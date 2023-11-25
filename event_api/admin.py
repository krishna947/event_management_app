from django.contrib import admin
from event_api import models

# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.Booking)
admin.site.register(models.CustomUser)