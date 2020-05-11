from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class item(models.Model):

    itemName= models.CharField(max_length=100)
    itemCatagory= models.CharField(max_length=100)
    catagoryID= models.IntegerField()
    hasSubcat= models.BooleanField(default=False)
    defaultVarient= models.CharField(max_length=20)
    itemPrice= models.IntegerField()
    hasStock= models.BooleanField(default=False)
    itemStock= models.IntegerField()
    maxBuy= models.IntegerField()
    itemImage= models.ImageField(upload_to='pictures')

class catagory(models.Model):
    catName= models.CharField(max_length=100)
    catType= models.CharField(max_length=100)
    catImage= models.ImageField(upload_to='pictures')

class usercart(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()

class userorders(models.Model):
    user_id = models.IntegerField()
    ammount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)
    total_items = models.IntegerField()
    
class orderdetails(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    pincode = models.IntegerField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()