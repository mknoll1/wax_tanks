from django.db import models

class WaxTank(models.Model):
    description = models.CharField(max_length=255)
    desired_temp = models. IntegerField(default=0)
    sensor_id = models.CharField(max_length=255)
    

class WaxTankReading(models.Model):
    wax_tank = models.ForeignKey(WaxTank)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField(default=0)
    heat_active = models.Boolean(default=False)

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()

class WorkDay(models.Model):
    employee = models.ForeignKey(Employee)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTImeField()
    break_time = models.IntegerField()

