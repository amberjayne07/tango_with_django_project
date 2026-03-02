from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin):
    populated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)


# Register your models here.