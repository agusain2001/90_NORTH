import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = data['sender']
        receiver = data['receiver']

        sender_user = User.objects.get(username=sender)
        receiver_user = User.objects.get(username=receiver)
        Message.objects.create(sender=sender_user, receiver=receiver_user, content=message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
            }
        )

    def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))