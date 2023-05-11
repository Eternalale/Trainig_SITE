from django.db import models


from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_or_end_task = models.BooleanField(default=False)
    date_or_time_create = models.DateTimeField(auto_now_add=True)
    date_or_time_update = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Information'