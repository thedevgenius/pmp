from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    org = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'is_staff': True})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        return super().save(*args, **kwargs)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    

class Team(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_lead')
    members = models.ManyToManyField(User, related_name='team_members')

    def __str__(self):
        return f'{self.company} - {self.lead}'
    
