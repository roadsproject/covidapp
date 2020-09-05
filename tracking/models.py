from django.db import models

# Create your models here.
class Visit(models.Model):
    user_id         = models.ForeignKey(User,on_delete=models.CASCADE)
    business_id     = models.ForeignKey(Business,on_delete=models.CASCADE)
    #date            = models.DateField(auto_now_add=Ture)
    datetime            = models.DateTimeField(auto_now_add=True)
    is_in           = models.BooleanField()

class User(models.Model):
    user_id         = models.AutoField(primary_key=True)
    user_name       = models.CharField(max_length = 50)
    first_name      = models.CharField(max_length = 100)
    last_name       = models.CharField(max_length = 100)
    email           = models.EmailField()
    phone           = models.PositiveIntegerField()

class Business(models.Model):
    business_id     = models.AutoField(primary_key=True)
    business_name   = models.CharField(max_length = 200)
    contact_name    = models.CharField(max_length = 200)
    email           = models.EmailField()
    phone           = models.PositiveIntegerField()
