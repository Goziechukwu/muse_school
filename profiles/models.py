from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    purchase information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    """
    A user profile model for managing information about Instructors.
    """
    name = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='instructors/', blank=True, null=True)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ContactRequest from {self.name}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
