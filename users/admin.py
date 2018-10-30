from django.contrib import admin

from .models import Profile

# admin.site.site_header = "JustThoughts Admin"
admin.site.register(Profile)
