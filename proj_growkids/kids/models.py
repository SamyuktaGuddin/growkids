from django.db import models

# Create your models here.

class UserLogin(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

class contact(models.Model):
    name= models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

class trainer_reg(models.Model):
    firstname =models.CharField(max_length=200)
    qualification= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    phoneno= models.CharField(max_length=20)
    yearofexp= models.CharField(max_length=20)
    category = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)


class userprofile(models.Model):
    firstname =models.CharField(max_length=200)
    lastnaem= models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    parentname = models.CharField(max_length=200)
    parentnumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

class training_details(models.Model):
    category =models.CharField(max_length=200)
    trainer_name= models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    video = models.FileField(upload_to='video/')

class enroll(models.Model):
    category =models.CharField(max_length=200)
    trainer_name= models.CharField(max_length=200)
    studentname = models.CharField(max_length=200)
    studentemail= models.CharField(max_length=200)
    enrolldate= models.CharField(max_length=200)

class payment_details(models.Model):
    emailid = models.CharField(max_length=200)
    paidby = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    paydate = models.CharField(max_length=200)





