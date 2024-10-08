from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.contrib import messages


from django.shortcuts import get_object_or_404
import sys



def home(request):
    ca=Category.objects.all()
    for i in ca:
        print(ca)
    # ca=Category.objects.filter()
    # print(ca)
    
    return render(request,'home.html')
def product(request):
    return render(request,'about.html')
def categories(request):
    return render(request,'categories.html')
def product_list(request):
    products=Product.objects.all()
    return render(request,'product_list.html',{'products':products})
def product_details(request,pk):
    products=Product.objects.get(pk=pk)
    return render(request,'product_details.html',{'product':products})
def cart(request,pk):
    products=Product.objects.get(pk=pk)
    return render(request,'cart.html',{'product':products})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        messages = request.POST.get('messages')


        if not name or not email or not messages:
            messages.error(request,"All fields are required.")
            return render(request,'contact.html')
        
        messages.success(request,"Your message has been sent")
        return redirect('contact')
    
    return render(request,'contact.html')

def product_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.POST.get('image')

        


        
    
    return render(request,'product_begin.html')

def registration_view(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Save the user to the database
        user.save()
        
        # Optionally authenticate and log the user in right after registration
        # user = authenticate(username=username, password=password)
        # login(request, user)
        
        # Redirect to login page after registration
        login(request,user)
        return redirect('login')
    
    return render(request, 'registration.html')
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)


            if user.is_superuser:
                return redirect('admin_view')  
            
            else:
                return redirect('product_list')
        else:
            return redirect('login')
    
    return render(request,'login.html')

def admin_view(request):

    if not request.user.is_superuser:
        messages.error(request,"you do not have permission to access the admin dashboard.")
        return redirect('product_list')
    
    return render(request,'admin.html')





def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    try:
        cart_item =Cart.objects.get(products=product,user=request.user)
        cart_item.quantity += 1
    except Cart.DoesNotExist:
        cart_item = Cart.objects.create(products=product, user=request.user, quantity=1)

    cart_item.save()
    return redirect('product_list')        

    
        
    
    

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.products.price * item.quantity for item in cart_items)
    return render(request,'cart.html',{'cart_items':cart_items ,'total_price':total_price})


def delete(request, id):
    try:
        # Get the cart item using the ID provided
        cart_item = Cart.objects.get(id=id, user=request.user)
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    except Cart.DoesNotExist:
        messages.error(request, "Item not found in cart.")

    return redirect('product_list')





def place_order(request):
    cartitems = Cart.objects.filter(user=request.user)
    if not cartitems.exists():
        return redirect('product_list')
    existing_order = Order.objects.filter(user=request.user).first()

    if request.method=='POST':
        address = request.POST.get('address')
        if existing_order:
            existing_order.address=address
            existing_order.save()

        else:
            order=Order.objects.create(user=request.user,address=address)

        return redirect('order_confirmation')
    return render(request,'place_order.html',{'user':request.user,'cartitems':cartitems,'existing_address':existing_order.address if existing_order else ''})        
    

def order_confirm(request):
    # Fetch the latest order placed by the user
    order = Order.objects.filter(user=request.user).first()

    if not order:
        return redirect('place_order')  # If no order exists, redirect to place an order

    # Render the order confirmation page with order details
    return render(request, 'order_confirmation.html')

from .forms import CategoryForm,ProductForm


def create_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form}) 

def create_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})  

def delete(request,id):
    if request.method == 'POST':
        product=Product.objects.get(pk=id)
        product.delete()
        return redirect('product_list')
    return redirect('product_list')


def edit(request,product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()

        return redirect('product_list')
    

    return render(request,'edit.html',{product:'product'})

def category_view(request):
    
        name = request.POST.get('name')
        
        image = request.POST.get('image')
        number = request.POST.get('number')


        


        
    
        return render(request,'categories.html')



# Create your views here.
