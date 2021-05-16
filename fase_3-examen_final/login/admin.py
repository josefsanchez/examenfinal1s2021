"""
    Se registra la clase de userprofile en el panel de administración
"""

from login.models import UserProfile
from django.contrib import admin 

admin.site.register(UserProfile)