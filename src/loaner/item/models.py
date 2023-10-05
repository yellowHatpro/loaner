from django.db import models
from enum import Enum
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, name, email, annual_income, aadhar_id, password, **other_fields):
  
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        return self.create_user(name, email, annual_income, aadhar_id, password, **other_fields)

    def create_user(self, name, email, annual_income, aadhar_id, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        if not name:
            raise ValueError(_('You must provide a name'))
        if not annual_income:
            raise ValueError(_('You must provide an annual income'))
        if not aadhar_id:
            raise ValueError(_('You must provide your aadhar id'))
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, annual_income=annual_income, aadhar_id=aadhar_id, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.CharField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=36
    )
    name = models.CharField(max_length=255)
    email = models.EmailField( _("email address"), unique=True)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    aadhar_id = models.CharField(max_length=36, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['annual_income', 'name', 'aadhar_id']

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user',
        to_field='aadhar_id'
    )
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=6)
    amount = models.FloatField()

    def __str__(self):
        return str(self.id)