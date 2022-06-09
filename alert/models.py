from django.db import models

# Create your models here.

class Alert(models.Model):
    alert_rate = models.IntegerField(max_length=5)

    def __str__(self):
        return str(self.alert_rate)