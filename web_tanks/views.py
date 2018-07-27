from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from web_tanks.models import *


# Create your views here.
@require_POST
def tank_reading(request)
    tanks 
