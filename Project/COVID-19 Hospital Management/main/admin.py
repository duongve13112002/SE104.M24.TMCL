from django.contrib import admin
from .models import *
# Các phần sẽ có trong model dc khai bao ở đây.
admin.site.register(Patient)
admin.site.register(Bed)
admin.site.register(Doctor)