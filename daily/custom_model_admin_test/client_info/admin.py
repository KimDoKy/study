from django.contrib import admin
from .models import ClientInfo

class ClientAdmin(admin.ModelAdmin):
    model = ClientInfo

admin.site.register(ClientInfo, ClientAdmin)
