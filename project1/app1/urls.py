from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    # path('Category',views.Categor),
    # path('product',views.product),
    
    path('product_details/<int:pk>/',views.product_details,name='product_details'),
    path('cart/<int:pk>',views.cart,name='cart'),
    path('contact/',views.contact_view,name='contact'),
    path('product_begin/',views.product_view,name='product_begin'),
    path('products/', views.product_list, name='product_list'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('add/<int:id>/',views.add_to_cart, name='add_to_cart'),
    path('place_order/',views.place_order,name='place_order'),
    path('order-confirmation/', views.order_confirm, name='order_confirmation'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('create_category/',views.create_category,name='create_category'),
    path('create_product/',views.create_product,name='create_product'),
    path('admin_view',views.admin_view,name='admin_view'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:product_id>/',views.edit,name='edit'),
    path('category_view',views.category_view,name='category_view')
    
]
