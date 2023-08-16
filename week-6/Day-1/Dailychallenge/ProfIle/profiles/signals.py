# profiles/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile  # Use the correct import path

@receiver(post_save, sender=Profile)
def notify_new_profile(sender, instance, created, **kwargs):
    if created:
        print(f"New profile created - Name: {instance.name}, Email: {instance.email}")
