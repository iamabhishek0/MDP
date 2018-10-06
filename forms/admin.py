from django.contrib import admin
from .models import FormSubmit , ReferenceMail

admin.site.site_header = "MDP ADMIN PAGE";
admin.site.site_title = "ADMISTRATOR";


class AllEntiryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
class AllEntiryAdmin1(admin.ModelAdmin):
    list_display = ( "reference_name","reference_email")    

admin.site.register(FormSubmit,AllEntiryAdmin)   
admin.site.register(ReferenceMail,AllEntiryAdmin1)   