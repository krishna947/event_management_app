# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name


class Event(models.Model):
    EVENT_CHOICES = [
        ('online', 'Online Event'),
        ('offline', 'Offline Event'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)  # Online or offline event
    max_seats = models.PositiveIntegerField()
    booking_open_window_start = models.DateTimeField()
    booking_open_window_end = models.DateTimeField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_events')

    def is_booking_open(self):
        from django.utils import timezone
        now = timezone.now()
        return self.booking_open_window_start <= now <= self.booking_open_window_end
    
    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)


