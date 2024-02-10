from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from store_app.models import User

User = get_user_model()

# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='billing')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.TextField(max_length=200, blank=True, null=True)
    address2 = models.TextField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return f"{self.user}'s billing address"


    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True
    



@receiver(post_save, sender = User)
def create_billing(sender, instance, created, **kwargs):
    if created:
        BillingAddress.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_billing(sender, instance, **kwargs):
    instance.profile.save()