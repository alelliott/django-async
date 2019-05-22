import time
import json

from {{project_name}}.celery import app
from applications.example_task.models import Task

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@app.task
def example_task_function(input_text):
    # time sleep represents a long running process
    time.sleep(3)

    # Change task status to completed
    task = Task.objects.get(name=input_text)
    task.status = "completed"
    task.save()

    response = {
        "action": "completed",
        "task_id": task.id,
        "task_name": task.name,
        "task_status": task.status,
    }

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "taskstatus",
        {
            "type": "update.task",
            "text": json.dumps(response),
        },
    )
