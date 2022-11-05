from django.db import models

# Create your models here.
class Todo_list_model(models.Model):
    task = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task