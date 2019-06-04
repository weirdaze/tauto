from django.contrib import admin
from .models import DeviceModel, DeviceType

# Register your models here.
admin.site.register(DeviceModel)
admin.site.register(DeviceType)