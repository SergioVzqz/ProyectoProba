from django.contrib import admin
from .models import *


# Register your models here.
@adming.resgister(Covid)
class ViewAdmin(admin.ModelAdmin):
