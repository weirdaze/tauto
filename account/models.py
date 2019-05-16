# Create your models here.
from django.db import models
import random
import string
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    phone = models.CharField(blank=True, max_length=50)
    company = models.CharField(max_length=200)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=200, default='xx', blank=True)
    active = models.BooleanField(default=False)
    accepted_eula = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def secure_rand(self, len=8):
        token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=len))
        return self.user.username + str(token)

    def save(self, *args, **kwargs):
        """
        If this is a new user, generate code.
        Otherwise leave as is
        """
        if not self.pk:
            self.code = self.secure_rand()
            print("refer code: " + self.code)

        return super(Profile, self).save(*args, **kwargs)

