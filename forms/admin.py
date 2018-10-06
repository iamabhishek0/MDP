from django.contrib import admin
from .models import FormSubmit

admin.site.site_header = "MDP ADMIN PAGE";
admin.site.site_title = "ADMISTRATOR";


# Register your models here.
class AllEntiryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
admin.site.register(FormSubmit,AllEntiryAdmin)   