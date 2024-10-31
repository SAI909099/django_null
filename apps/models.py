from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):


    def clean(self):
        if self.username.lower() == "botir":
            raise ValidationError(" botir degan username qo'yib bo'lmaydi ")


