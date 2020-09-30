from django.db import models
from datetime import datetime

# Create your models here.
class HafaSamband(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    lemma_id = models.IntegerField()
    lemma = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=False)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.lemma
