from django.db import models

# Create your models here.

class Contract(models.Model):
    address = models.CharField(max_length = 250)
    phone = models.CharField(max_length = 250)
    mobile = models.CharField(max_length = 250)
    email = models.EmailField()

    def __str__(self):
        return str(self.mobile)