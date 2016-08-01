from django.contrib import admin

# Register your models here.
from loginsys.models import UserProfile

admin.site.register(UserProfile)