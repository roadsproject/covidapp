from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# class User(models.Model):
#     user_id         = models.AutoField(primary_key=True)
#     user_name       = models.CharField(max_length = 50)
#     first_name      = models.CharField(max_length = 100)
#     last_name       = models.CharField(max_length = 100)
#     email           = models.EmailField()
#     phone           = models.PositiveIntegerField()

# class Business(models.Model):
#     business_id     = models.AutoField(primary_key=True)
#     business_name   = models.CharField(max_length = 200)
#     contact_name    = models.CharField(max_length = 200)
#     email           = models.EmailField()
#     phone           = models.PositiveIntegerField()

class User(AbstractUser):
    is_individual           = models.BooleanField(default=False)
    is_business             = models.BooleanField(default=False)
    phone                   = models.CharField(max_length = 50,blank=True)

class Individual(models.Model):
    i_user            = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    #individual_id   = models.AutoField(primary_key=True)
    #user_name       = models.CharField(max_length = 50)
    first_name      = models.CharField(max_length = 100)
    last_name       = models.CharField(max_length = 100)
    email           = models.EmailField()
    phone           = models.CharField(max_length = 50) #changed to show numbers better
    #password        = models.CharField(max_length = 32)


class Business(models.Model):
    #b_user            = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    business_id     = models.AutoField(primary_key=True)
    business_name   = models.CharField(max_length = 200)
    contact_name    = models.CharField(max_length = 200)
    email           = models.EmailField()
    phone           = models.CharField(max_length = 50)

class Visit(models.Model):
    user_id                  = models.ForeignKey(User,on_delete=models.CASCADE)
    business_id         = models.ForeignKey(Business,on_delete=models.CASCADE)
    #business_id       = models.ForeignKey(Business,on_delete=models.CASCADE)
    #date             = models.DateField(auto_now_add=Ture)
    datetime          = models.DateTimeField(auto_now_add=True)
    #is_in             = models.BooleanField()
    IN = 'IN'
    OUT = 'OUT'
    RECORD_TYPES =[(IN,'I am sign in'),(OUT,'I am sign out'),]
    record_type = models.CharField(max_length = 3,choices = RECORD_TYPES, default = IN,)