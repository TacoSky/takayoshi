from django.contrib import admin

# Register your models here.

from .models import Company,JobeRole,Experience

admin.site.register(Company)
admin.site.register(JobeRole)
admin.site.register(Experience)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

