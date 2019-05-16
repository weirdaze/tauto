from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .device import Device
from .tasks import add

# Create your views here.


'''name = ''
serdes_num_front = ''
serdes_num_fabric = ''
serdes_speed_front = ''
serdes_speed_fabric = ''
model = ''
macs = []

chipset = {
    'name': name,
    'serdes_num_front': serdes_num_front,
    'serdes_num_fabric': serdes_num_fabric,
    'serdes_speed_front': serdes_speed_front,
    'serdes_speed_fabric': serdes_speed_fabric,
    'model': model,
}


name = ''
chipsets = []

module_build = {
    'name': name,
    'chipsets': chipsets,
}


name = ''
module_type = ''
ip = ''
module_build = ''
chassis = ''
slot = ''
serial = ''
state = ''


module = {
    'name': name,
    'module_type': module_type,
    'ip': ip,
    'module_build': module_build,
    'chassis': chassis,
    'slot': slot,
    'serial': serial,
    'state': state,
}

name = ''
description = ''
type = ''
slot = ''
number = ''
mac_addr = ''
ip = ''
speed = ''
state = ''
verified = ''
tx_bandwidth_utilization = ''
rx_bandwidth_utilization = ''


interface = {
    'name': name,
    'description': description,
    'type': type,
    'slot': slot,
    'number': number,
    'mac': mac_addr,
    'ip': ip,
    'speed': speed,
    'state': state,
    'verified': verified,
    'tx_bandwidth_utilization': tx_bandwidth_utilization,
    'rx_bandwidth_utilization': rx_bandwidth_utilization,
}

hostname = ''
fqdn = ''
serial = ''
model = ''
mac_addr = ''
num_slots = ''
state = ''
modules = []
interfaces = []

device = {
    'hostname': hostname,
    'fqdn': fqdn,
    'serial': serial,
    'mac': mac_addr,
    'num_slots': num_slots,
    'state': state,
    'model': model,
    'modules': modules,
    'interfaces': interfaces,
}'''


@shared_task
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
    print(add(5, 3))
    return HttpResponse("<h1>Hello</h1>")


@csrf_exempt
def device_create(request):
    if request.method == 'POST':
        pass
