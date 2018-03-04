from django.contrib import admin

# Register your models here.

from .models import Company,JobeRole,Experience,Classification,Portfolio


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'description')
    ordering = ('order',)


class JobRoleAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'description')
    ordering = ('order',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'type', 'incharge', 'keyword', 'achievement')
    ordering = ('order',)


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    ordering = ('name',)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'achievement')
    ordering = ('order',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(JobeRole, JobRoleAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Portfolio, PortfolioAdmin)