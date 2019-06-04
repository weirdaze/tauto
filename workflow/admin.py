from django.contrib import admin
from .models import Step, StepType, StepState, StepAction

# Register your models here.
admin.site.register(Step)
admin.site.register(StepType)
admin.site.register(StepState)
admin.site.register(StepAction)