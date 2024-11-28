from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICE = (
        ('LD', 'Leader'),
        ('MB', 'Member')
    )
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=3, default='MB', choices=ROLE_CHOICE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        return super().save(*args, **kwargs)


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'LD'}, related_name='team')
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    

class Designation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'MB'})
    deg = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('team', 'member',)
    
    def __str__(self):
        return f'{self.team} - {self.member.first_name} {self.member.last_name}'
    


