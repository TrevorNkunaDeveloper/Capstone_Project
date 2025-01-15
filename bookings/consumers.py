"""
This module defines a WebSocket consumer for handling real-time booking connections.

Classes:
    BookingConsumer: An asynchronous WebSocket consumer that manages real-time
                     communication for bookings. It handles WebSocket connection
                     establishment and sends an initial connection confirmation message.

Methods:
    connect(): Handles the WebSocket connection when a client connects. Sends a
               JSON-formatted message confirming the connection.
"""
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BookingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({'message': 'Connected!'}))
