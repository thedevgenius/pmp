from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.dispatch import Signal
user_created = Signal()


@receiver(user_created)
def create_team_member(sender, request, user, **kwargs):
    team = Team.objects.get(request.user)
    TeamMember.objects.create(
        team=team,
        member=user
    )
    print('team Member Created')