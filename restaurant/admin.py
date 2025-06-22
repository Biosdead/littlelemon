from django.contrib import admin
from .models import booking,menu,User

# Register your models here.
admin.site.register(booking)
admin.site.register(menu)
admin.site.register(User)