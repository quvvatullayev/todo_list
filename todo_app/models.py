from django.db import models

# Create your models here.
class Todo_list_model(models.Model):
    task = models.TextField()
    status = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()