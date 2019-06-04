from __future__ import absolute_import, unicode_literals
from celery import shared_task
import pyeapi
import time
from datetime import datetime
# Create your tasks here


class Device:
    def __init__(self, device_context):
        print("fqdn: " + device_context['fqdn'])
        pass

#@shared_task
def index(request):
    '''
        devices = [
            {
                'fqdn': 'yo410.sjc.aristanetworks.com',
            },
            {
                'fqdn': 'yo653.sjc.aristanetworks.com',
            },
        ]
    '''

    context = {
        'fqdn': 'yo410.sjc.aristanetworks.com'
    }
    my_device = Device(context)
    #print(add(5, 3))
    #return HttpResponse("<h1>Hello</h1>")


#@csrf_exempt
def device_create(request):
    if request.method == 'POST':
        pass
