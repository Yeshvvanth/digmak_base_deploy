from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name='home'),
    path('accounts/signup/customer/', views.customerSignup, name='customer_register'),
    path('accounts/signup/accountant/', views.accountantSignup, name='accountant_register'),
    path('accounts/login/customer', views.customerLogin, name='customer_login'),
    path('accounts/login/accountant', views.accountantLogin, name='accountant_login'),
    path('accounts/logout/',views.logoutUser,name='logout'),
    path('customer/profile',views.customerProfile,name='customer_profile'),
    path('customer/home',views.customerHome,name='customer_home'),
    path('accountant/profile',views.accountantProfile,name='accountant_profile'),
    path('accountant/home',views.accountantHome,name='accountant_home')


  

]
