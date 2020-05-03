from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)

    class TodoStatus(models.TextChoices):
        WAITING = 'WAITING', 'Waiting'
        WORKING = 'WORKING', '進行中'
        DONE = '完了', 'DONE'

    status = models.CharField(
        max_length=7,
        choices=TodoStatus.choices,
        default=TodoStatus.WAITING
    )

    def __str__(self):
        return self.title
