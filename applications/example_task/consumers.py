import json
from time import time
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from applications.example_task.models import Task
from applications.example_task.tasks import example_task_function


class TaskConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        layer_identifier = "taskstatus"
        self.layer_identifier = layer_identifier
        await self.channel_layer.group_add(layer_identifier, self.channel_name)

        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        await self.channel_layer.group_discard(self.layer_identifier, self.channel_name)

    async def websocket_receive(self, event):
        print("receive", event)
        receive_message = event.get('text', None)

        if receive_message is not None:
            loaded_dict_data = json.loads(receive_message)
            input_text = loaded_dict_data.get('message')

            # Save object in database
            # await self.create_new_object(input_text)
            new_task = await self.create_new_task(input_text)

            response = {
                "action": "started",
                "task_id": new_task.id,
                "task_name": new_task.name,
                "task_status": "started",
            }

            # Start task
            example_task_function.delay(new_task.name)

            # Broadcast message
            await self.channel_layer.group_send(
                self.layer_identifier,
                {
                    "type": "new.object",
                    "text": json.dumps(response),
                },
            )

    async def new_object(self, event):
        # Send message
        await self.send({
            'type': "websocket.send",
            'text': event['text']
        })

    async def update_task(self, task):
        # Send message
        await self.send({
            'type': "websocket.send",
            'text': task['text']
        })

    @database_sync_to_async
    def create_new_task(self, task):
        return Task.objects.create(
            name=task,
            status="started",
        )
