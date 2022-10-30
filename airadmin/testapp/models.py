from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class airport(models.Model):
    country = models.CharField(max_length=100)
    A_id = models.IntegerField()
    A_name = models.CharField(max_length=100)

class airline_company(models.Model):
    flight_id = models.CharField(max_length=10)
    airline_name = models.CharField(max_length=100)

class flight(models.Model):
    f_id = models.ForeignKey(airline_company, on_delete=models.CASCADE)
    f_time = models.TimeField(default=None)
    f_date = models.DateField(default=None)
    f_from = models.CharField(max_length=50, default=None)
    f_to = models.CharField(max_length=50, default=None)
    f_status = models.CharField(max_length=20, default=None)
    status = models.CharField(max_length=50, default=None)

class employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    E_id = models.IntegerField(unique=True, default=None)
    E_name = models.CharField(max_length=30, default=None)
    E_password = models.CharField(max_length=15, default=None)
    E_c_password = models.CharField(max_length=15, default=None)
    E_pno = models.IntegerField(default=0)
    E_address = models.TextField(default=None)
    E_salary = models.FloatField(default=0.00)
    E_designation = models.CharField(max_length=25, default=None)
    E_department = models.CharField(max_length=100, default='undefined')
    E_age = models.IntegerField(default=0)
    E_gender = models.CharField(max_length=5, default='Male')
    E_email = models.EmailField(max_length=30, default=None)
    user_type = models.CharField(max_length=50, default="emp")

class passenger(models.Model):
    flight_id = models.ForeignKey(airline_company, on_delete=models.CASCADE, default=None)
    P_id = models.IntegerField(unique=True, default=0)
    P_status = models.CharField(max_length=10, default=None)
    P_age = models.IntegerField(default=0)
    P_name = models.CharField(max_length=50, default=None)
    P_gender = models.CharField(max_length=5, default=None)

class immigration(models.Model):
    E_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    P_name = models.ForeignKey(passenger, on_delete=models.CASCADE)
    E_name = models.CharField(max_length=50)

class runway(models.Model):
    flight_id = models.ForeignKey(airline_company, on_delete=models.CASCADE,default=None)
    R_id = models.CharField(max_length=5, default=None)
    status_of_terminal = models.CharField(max_length=15,default="not occupied")
    date = models.DateField(default=None)
    lock_time = models.TimeField(default=datetime.now())
    release_time = models.TimeField(default=datetime.now())
class runway1(models.Model):
    flight_id = models.ForeignKey(airline_company, on_delete=models.CASCADE,default=None)
    R_id = models.CharField(max_length=5, default=None)
    status_of_terminal = models.CharField(max_length=15,default="not occupied")
    date = models.DateField(default=None)
    lock_time = models.TimeField(default=datetime.now())
    release_time = models.TimeField(default=datetime.now())
class runway2(models.Model):
    flight_id = models.ForeignKey(airline_company, on_delete=models.CASCADE,default=None)
    R_id = models.CharField(max_length=5, default=None)
    status_of_terminal = models.CharField(max_length=15,default="not occupied")
    date = models.DateField(default=None)
    lock_time = models.TimeField(default=datetime.now())
    release_time = models.TimeField(default=datetime.now())
class runway3(models.Model):
    flight_id = models.ForeignKey(airline_company, on_delete=models.CASCADE,default=None)
    R_id = models.CharField(max_length=5, default=None)
    status_of_terminal = models.CharField(max_length=15,default="not occupied")
    date = models.DateField(default=None)
    lock_time = models.TimeField(default=datetime.now())
    release_time = models.TimeField(default=datetime.now())
class runway4(models.Model):
    flight_id = models.ForeignKey(airline_company, on_delete=models.CASCADE,default=None)
    R_id = models.CharField(max_length=5, default=None)
    status_of_terminal = models.CharField(max_length=15,default="not occupied")
    date = models.DateField(default=None)
    lock_time = models.TimeField(default=datetime.now())
    release_time = models.TimeField(default=datetime.now())


class store(models.Model):
    S_id = models.IntegerField()
    S_equipment = models.CharField(max_length=25)
    S_price = models.FloatField()
    S_quantity = models.IntegerField()
    image=models.FileField(upload_to='images')