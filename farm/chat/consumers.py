# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        # user = self.scope["user"]  #이거 추가함
        # sender=user.username
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender':sender  #이거 추가 사항
            }
        )
        
        
        

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender=event['sender']
        # user = self.scope["user"]  #이거 추가함
        # sender=user.username

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender':sender,  #이거 추가 사항
        }))
        
        
#consumer.py는 모든 요청을 받아들이는 비동기적인 WebSocket 소비자 역할을 하게된다. 즉 메세지를 클라이언트로부터 받아서 그대로 클라이언트에게 전달하는 기능을 하게 된다.