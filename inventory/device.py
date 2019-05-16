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
