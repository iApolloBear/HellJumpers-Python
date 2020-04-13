from django.contrib import admin
from .models import UserWallet, Promocion, Client

# Register your models here.
admin.site.register(UserWallet)
admin.site.register(Promocion)
admin.site.register(Client)