from email.mime import message
from django.db import models
from django.utils import timezone

class Info(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.TextField(max_length=200, null=True, blank=True)
    message = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    class Meta:
    
        ordering = ['date']
        get_latest_by = 'date'
        verbose_name_plural = "Info"


    def __str__(self):
        return self.name


