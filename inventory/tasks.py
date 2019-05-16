from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    total = 4000000
    i = 0
    while True:
        if i < total:
            break
        i += 1
    return x + y
