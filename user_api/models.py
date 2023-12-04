
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('An email is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_regex = RegexValidator(
        regex=r'^0[5-7]\d{8}$',
        message='Phone number must be 10 digits and start with 05, 06, or 07.'
    )
    phone = models.CharField(validators=[phone_regex], max_length=10, unique=True, null=True, blank=False)
    nom = models.CharField(max_length=30, null=True, blank=False)
    prenom = models.CharField(max_length=30, null=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = AppUserManager()

    def clean(self):
        if self._state.adding:
            if not self.email:
                raise ValidationError({'email': 'Email is required.'})
            if not self.phone:
                raise ValidationError({'phone': 'Phone number is required.'})
            if not self.nom:
                raise ValidationError({'nom': 'Name is required.'})
            if not self.prenom:
                raise ValidationError({'prenom': 'Surname is required.'})

