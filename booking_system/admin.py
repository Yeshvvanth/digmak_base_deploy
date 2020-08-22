from django.contrib import admin
from .models import Customer,Accountant,User
# Register your models here.
admin.site.register(Customer)
admin.site.register(Accountant)
admin.site.register(User)

