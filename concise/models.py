from django.db import models

# Create your models here.
class stripurl(models.Model):
    org_url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=200, null=True)