from django.contrib import admin
from django.core.exceptions import AppRegistryNotReady
from .models import user_info
# Register your models here.
admin.site.register(user_info)
