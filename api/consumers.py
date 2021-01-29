from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from asyncio import sleep
import json

class NumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        self.room_group_name = "user_"+str(self.scope['url_route']['kwargs']['id'])
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def showDigits(self, event):
        await self.send(json.dumps({"text" : event['text']}))

    async def disconnect(self, close_code):
        print("disconnected")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # async def receive(self, text_data):
    #     data = json.loads(text_data)['winpath']
    #     user_id = data.split('/')[-2]
    #     self.room_group_name = "run_"+str(user_id)
    #     await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        
    