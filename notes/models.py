from django.db import models

# Create your models here.
class Note(models.Model):
    Date = models.DateTimeField ()
    title = models.CharField(max_length=50)
    body = models.TextField()


