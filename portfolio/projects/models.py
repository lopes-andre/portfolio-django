from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='images/') # Needs pillow installed
    summary = models.CharField(max_length=200)
