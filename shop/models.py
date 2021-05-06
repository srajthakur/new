from django.db import models

# Create your models here.
class product(models.Model):

    pid=models.AutoField
    pname=models.CharField(max_length=20)
    decs=models.CharField(max_length=50)
    date=models.DateField()
    ca=models.CharField(max_length=50,default="")
    sca=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.pname

class contact(models.Model):
    cid=models.AutoField
    cname=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=10,default="")
    desc=models.CharField(max_length=500,default="")


    def __str__(self):
        return self.cname

class Cart(models.Model):
    cid=models.AutoField
    cartid=models.CharField(max_length=50,default="")
    cartname = models.CharField(max_length=20,default="")
    cartdecs = models.CharField(max_length=50,default="")
    cartimage = models.ImageField(upload_to="shop/cartimage", default="")
    cartprice = models.IntegerField(default=0)

    def __str__(self):
        return self.cartid

class Login(models.Model):
    lid=models.AutoField
    loginid=models.CharField(max_length=50,default="")
    loginname = models.CharField(max_length=20,default="")
    password = models.CharField(max_length=50,default="")


    def __str__(self):
        return self.loginid