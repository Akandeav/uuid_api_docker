from django.db import models

class UUIDValue(models.Model):
    """
    API timestamp and UUID object
    """
    time_stamp = models.CharField(max_length=50)
    uuid = models.CharField(max_length=32)
