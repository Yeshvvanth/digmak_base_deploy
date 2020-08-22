from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
# Create your models here.


class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'customer'),
      (2, 'accountant'),
      (3, 'admin'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    citizenship = models.CharField(max_length=30)
    country_residence = models.CharField(max_length=30)
 


class Accountant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    citizenship = models.CharField(max_length=30)
    country_residence = models.CharField(max_length=30)
    tax_regulation_specialty = models.CharField(max_length=50)
    hour_rate = models.DecimalField(decimal_places=2, max_digits=12,blank=True,null=True)
    availability = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)


def create_profile(sender,instance,created,**kwargs):
    if created and instance.user_type==1:
        Customer.objects.create(user=instance)
        print("customer profile created")
    elif created and instance.user_type == 2:
        Accountant.objects.create(user=instance)
        print("accountant profile created")
post_save.connect(create_profile,sender = User)

def update_profile(sender,instance,created,**kwargs):
    if created == False:
        print()
        try:
            if instance.user_type==1:
                instance.customer.save()
                print('profile updated')
            elif instance.user_type==2:
                instance.accountant.save()
        except:
            if instance.user_type==1:
                Customer.objects.create(user=instance)
                print('profile created for existing user')
            elif instance.user_type==2:
                Accountant.objects.create(user=instance)

post_save.connect(update_profile,sender = User)

