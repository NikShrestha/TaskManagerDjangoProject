from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=200)

from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=200)

class Profile(models.Model):
    signup_username = models.CharField(max_length=150, blank=True)
    signup_password = models.CharField(max_length=128, blank=True)  # Assuming password hash length
    # Add additional fields if needed

    def save_signup_credentials(self, username, password):
        self.signup_username = username
        self.signup_password = password
        self.save()

