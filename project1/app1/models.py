from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=200)
    image=models.FileField(upload_to="category/images")
    number=models.IntegerField(null=True)
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=800)
    price=models.IntegerField()  
    image=models.FileField(upload_to="product/images") 


    
   

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username
    

class Order(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address
        

    

