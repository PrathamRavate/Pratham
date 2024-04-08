import uuid
from django.db import models

class Todo(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_title
