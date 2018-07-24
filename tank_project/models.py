from django.db import models

Class WaxTank(models.Model):
    description = models.CharField(max_length=255)
    desired_temp = models. IntegerField(default=0)
    

Class WaxTankReading(models.Model):
    wax_tank = models.ForeignKey(WaxTank)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField(default=0)
    heat_active = models.Boolean(default=False)

Class Employee(models.Model):

