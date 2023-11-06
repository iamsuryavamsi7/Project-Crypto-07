from django.contrib import admin
from travello.models import Destination


class DestinationAdmin(admin.ModelAdmin):
    list_display = ["place", "desc", "price"]


admin.site.register(Destination, DestinationAdmin)