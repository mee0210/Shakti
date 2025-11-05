from django.db import models
from django.contrib.auth.hashers import make_password

class WomanUser(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # ✅ Hash password
        super(WomanUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Officer(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    workplace = models.CharField(max_length=150)
    badge_id = models.CharField(max_length=100, unique=True)
    official_email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # ✅ Hash password
        super(Officer, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
