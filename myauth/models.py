from django.contrib.auth.models import User, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserModel(AbstractUser):
    pass
    # GENDER = (
    #     ('male', 'Male'),
    #     ('female', 'Female')
    # )
    # username = models.CharField(max_length=50, default=None)
    # password = models.CharField(max_length=50, default=None)
    # age = models.PositiveIntegerField()
    # gender = models.CharField(choices=GENDER, max_length=6)
    # phone_number = PhoneNumberField(default='0')
    # last_seen = models.DateTimeField(auto_now=True, blank=True, null=True)
    # profile_image = models.ImageField(upload_to='forum/images')

    # def __str__(self):
        # return self.user.username
