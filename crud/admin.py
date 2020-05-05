from django.contrib import admin
from .models import UserWallet, Promocion, Client, Concurso

# Register your models here.
admin.site.register(UserWallet)
admin.site.register(Promocion)
admin.site.register(Concurso)
admin.site.register(Client)