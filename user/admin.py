from django.contrib import admin
from user.models import User_Model, Address

# Register your models here.
admin.site.register(User_Model)
admin.site.register(Address)
