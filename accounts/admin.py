from django.contrib import admin
from .models import User, Role, UserManager

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserManager)