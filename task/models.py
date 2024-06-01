from django.db import models
from category.models import Category

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='tasks')
    
    def __str__(self) -> str:
        return self.title