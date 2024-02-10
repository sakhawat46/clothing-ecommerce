from django.db import models

# Create your models here.

class About(models.Model):
    at_a_glance = models.TextField()
    message_from_ceo = models.TextField()
    company_profile = models.TextField()
    our_concern = models.TextField()

    def __str__(self):
        return str(self.at_a_glance)