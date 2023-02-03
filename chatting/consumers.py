import json
from pprint import pprint

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from . import models


class ChatConsumer(AsyncWebsocketConsumer):
    '''asynchornous chat consumer'''

    @database_sync_to_async
    def create_chat(self, message, sender):
        s, _ = models.Sender.objects.get_or_create(
            name = sender
        )
        m = models.Message.objects.create(content=message, sender=s)
        m.save()
        return m

    async def connect(self):
        print('connected')
        self.group_name = 'chatco'

        # join a room group:
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):

        # leave a room group:
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # receive messages from websocket:
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        m = await self.create_chat(message, sender)

        # send message to room group:
        await self.channel_layer.group_send(
            self.group_name, {
                'type': 'chat_message', 
                'content': m.content,
                'sender': m.sender.name,
                'timestamp': m.timestamp.isoformat(),
            }
        )

    # receive messages from room group:
    async def chat_message(self, event):
        content = event['content']
        sender = event['sender']
        timestamp = event['timestamp']
        print(event)
        # send message to websocket:
        await self.send(text_data=json.dumps({
            'content': content,
            'sender': sender,
            'timestamp': timestamp,
        }))
    
