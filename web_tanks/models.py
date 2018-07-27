from __future__ import unicode_literals

from django.db import models

# Create your models here.


class WaxTank(models.Model):
    description = models.CharField(max_length=255)
    desired_temp = models. IntegerField(default=0)
    sensor_id = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s (%s): %s' % (self.description, self.sensor_id, self.desired_temp)
    

class WaxTankReading(models.Model):
    wax_tank = models.ForeignKey(WaxTank)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField(default=0)
    heat_active = models.BooleanField(default=False)
