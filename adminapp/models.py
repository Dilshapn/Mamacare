from django.db import models


# Create your models here.
class Doctor_db(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Qualification = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Interest = models.CharField(max_length=50,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Hospital = models.CharField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=50,null=True,blank=True)
    District = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to="photos",null=True,blank=True)

class Category_db(models.Model):
    category = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to="pictures",null=True,blank=True)

class book_db(models.Model):
    book_name = models.CharField(max_length=50,null=True,blank=True)
    author = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="books",null=True,blank=True)

class product_db(models.Model):
    category = models.CharField(max_length=50,null=True,blank=True)
    item = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    image1 = models.ImageField(upload_to="picture", null=True, blank=True)
    image2 = models.ImageField(upload_to="picture", null=True, blank=True)
    image3 = models.ImageField(upload_to="picture", null=True, blank=True)

