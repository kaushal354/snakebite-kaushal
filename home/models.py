from django.db import models

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    hospital_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    cobra_antidote = models.BooleanField(default=False)
    python_antidote = models.BooleanField(default=False)
    russel_antidote = models.BooleanField(default=False)

    def __str__(self):
        return self.hospital_name
