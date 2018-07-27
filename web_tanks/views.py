from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from web_tanks.models import *


# Create your views here.
@require_POST
@csrf_exempt
def all_tank_reading(request):
    context = {}
    tanks = WaxTank.objects.all()
    wax_tank_readings = ()
    max_difference = 0
    max_difference_tank_sensor = None
    for tank in tanks:
        wax_tank_reading = WaxTankReading.objects.create(
            wax_tank=tank,
            temperature=request.POST.get(tank.sensor_id, tank.desired_temp),
            heat_active=False
        )
        # See if this tank has a higher difference than any other tank
        if tank.desired_temp - wax_tank_reading > max_difference:
            max_difference = tank.desired_temp - wax_tank_reading
            max_difference_tank_sensor = tank.sensor_id
            max_reading = wax_tank_reading
        wax_tank_readings.add(wax_tank_reading)
        context[tank.sensor_id:False]
    if max_difference_tank_sensor:
        max_reading.heat_active = True
        max_reading.save()
        context[tank.sensor_id] = True

    return JsonResponse(context)



