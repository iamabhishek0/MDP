from django.contrib import admin
from .models import FormSubmit , ReferenceMail, Booking , Room
from django.contrib.auth.models import User, Group

admin.site.site_header = "MDP ADMIN PAGE";
admin.site.site_title = "ADMISTRATOR";


class AllEntiryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email","arrive","depart","reference_name","reference_email")
class AllEntiryAdmin1(admin.ModelAdmin):
    list_display = ( "reference_name","reference_email")
class RoomEntry(admin.ModelAdmin):
    list_display = ( "roomID", "room_type", "status")
class BookingEntry(admin.ModelAdmin):
    list_display = ( "bookingID", "roomID", "arrive", "depart")

admin.site.register(FormSubmit,AllEntiryAdmin)
admin.site.register(ReferenceMail,AllEntiryAdmin1)
admin.site.register(Room,RoomEntry)
admin.site.register(Booking,BookingEntry)

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'is_active']

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
#admin.site.unregister(User)
admin.site.unregister(Group)
