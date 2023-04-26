from django.contrib import admin
from . models import Company, Daybook, Techsupport

# Register your models here.
admin.site.register(Company)
admin.site.register(Daybook)
admin.site.register(Techsupport)