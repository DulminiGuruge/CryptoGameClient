""" # chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessages

from .models import ChatMessages  # new import


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope['user']  # new

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        # Load and send previous messages when a new user joins
        #self.send_previous_messages()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        if not self.user.is_authenticated:  # new
            return 
                

        # Save message to the database
        ChatMessages.objects.create(sender=self.user, content=message)  # new
      
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", 'user': self.user.username,"message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "sender":sender}))

    async def send_previous_messages(self):
        # Retrieve previous messages from the database
        messages = ChatMessages.objects.all().order_by('timestamp')[:10]

        for message in messages:
            self.send(text_data=json.dumps({
                'message': {
                    'sender': message.sender,
                    'content': message.content,
                }
            }))  """   



# chat/consumers.py
# import json

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer

# from .models import ChatMessages  # new import


# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"
#         self.user = self.scope['user']  # new

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", 'user': self.user.username,"message": message}
#         )
#           # Save message to the database
#         ChatMessages.objects.create(sender=self.user, content=message)  # new
      
       

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event["message"]
        

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({"message": message}))



# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
#from .models import ChatMessages  # new import

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope['user']  # new


        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message",'user': self.user.username, "message": message}
        )

        # Save message to the database using database_sync_to_async
        #await self.save_to_database(self.user, message)

           # Save message to the database
        #ChatMessages.objects.create(sender=self.user, content=message)  # new
      
   # @database_sync_to_async
   # def save_to_database(self, user, message):
        # Save message to the database
       # ChatMessages.objects.create(sender=user, content=message)

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))