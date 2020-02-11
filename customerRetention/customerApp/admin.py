from django.contrib import admin
from .models import *
# Register your models here.


class FruitHutAdmin(admin.ModelAdmin):

    list_display = ['catergory','units','datenew']
    list_filter = ['catergory']
    search_fields = ['catergory']

admin.site.register(Fruithut,FruitHutAdmin)
