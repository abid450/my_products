from django.db import models
# Create your models here.
class Products_M(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=150, unique=True)
    title = models.TextField()

    def __str__(self):
        return self.email_address
