from django.contrib import admin
from .models import FormSubmit , ReferenceMail, Booking , Room
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from  .models import UserProfile

admin.site.site_header = "MDP ADMIN PAGE";
admin.site.site_title = "ADMISTRATOR";


class AllEntiryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email","arrive","depart","reference_name","reference_email")
class AllEntiryAdmin1(admin.ModelAdmin):
    list_display = ( "reference_name","reference_email")
class RoomEntry(admin.ModelAdmin):
    list_display = ( "roomID", "room_type", "status")
class BookingEntry(admin.ModelAdmin):
    list_display = ( "bookingID", "roomID", "name", "arrive", "depart")

admin.site.register(FormSubmit,AllEntiryAdmin)
admin.site.register(ReferenceMail,AllEntiryAdmin1)
admin.site.register(Room,RoomEntry)
admin.site.register(Booking,BookingEntry)


class ProfileInline(admin.TabularInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ( 'id','first_name','email', 'is_staff', 'is_active')
    list_select_related = ('userprofile', )

    def get_reference_verified(self, instance):
        return instance.userprofile.reference_verified
    get_reference_verified.short_description = 'reference_verified'
    def get_director_verified(self, instance):
        return instance.userprofile.reference_verified
    get_director_verified.short_description = 'director_verified'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
