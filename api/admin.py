from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Image, Car

admin.site.register(User)
admin.site.register(Image)
admin.site.register(Car)
