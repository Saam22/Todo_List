from django.contrib import admin
from .models import Task
# Register your models here.
admin.site.site_header = "TODO List Admin"
admin.site.register(Task)