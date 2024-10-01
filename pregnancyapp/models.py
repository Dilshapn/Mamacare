from django.db import models

# Create your models here.
class patient_db(models.Model):
    doctor_name = models.CharField(max_length=100,null=True,blank=True)
    patient_name = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

class register_db(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)

class cart_db(models.Model):
    User_Name = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)

class proceed_db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Town = models.CharField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Pincode = models.IntegerField(null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    total_price = models.IntegerField(null=True,blank=True)

class wishlist(models.Model):
    user_name = models.CharField(max_length=100,null=True,blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="picture", null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)





