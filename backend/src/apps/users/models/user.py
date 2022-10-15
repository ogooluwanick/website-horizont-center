from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.contrib.postgres.fields import CIEmailField
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):

    def create_superuser(self, email: str = None, password: str = None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.password = make_password(password)
        user.save()
        return user


class User(AbstractUser):
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    objects = UserManager()

    email = CIEmailField(
        verbose_name=_('email'),
        db_index=True,
        unique=True
    )
    username = None
    first_name = models.CharField(
        null=False,
        blank=False,
        verbose_name=_('first name'),
        max_length=250,
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        verbose_name=_('last name'),
        max_length=250,
    )
    phone_number = models.CharField(
        verbose_name=_('phone number'),
        max_length=250,
    )
    second_phone_number = models.CharField(
        null=True,
        blank=True,
        verbose_name=_('second phone number'),
        max_length=250,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'password']
