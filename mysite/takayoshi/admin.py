from django.contrib import admin

# Register your models here.

from .models import Company,JobeRole,Experience


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'description')
    ordering = ('order',)


class JobRoleAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'description')
    ordering = ('order',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'type', 'incharge', 'keyword', 'achievement')
    ordering = ('order',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(JobeRole, JobRoleAdmin)
admin.site.register(Experience, ExperienceAdmin)