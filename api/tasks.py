from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from time import sleep

channel_layer = get_channel_layer()

@shared_task
def showNumbers(userid):
    for i in range(20):
        async_to_sync(channel_layer.group_send)("user_"+str(userid), {'type': 'showDigits', 'text' : i})
        sleep(1)