from django.contrib import admin
from .models import Rating, User, Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(User)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating)
