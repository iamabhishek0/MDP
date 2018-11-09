from django.contrib import admin
from .models import FormSubmit , ReferenceMail, Booking , Room,UserProfile
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from  .models import UserProfile

admin.site.site_header = "MDP ADMIN PAGE";
admin.site.site_title = "ADMISTRATOR";

class AllEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email","arrive","depart","reference_name","reference_email")
class AllEntryAdmin1(admin.ModelAdmin):
    list_display = ( "reference_name","reference_email")
class RoomEntry(admin.ModelAdmin):
    list_display = ( "roomID", "room_type", "status")
class BookingEntry(admin.ModelAdmin):
    list_display = ( "bookingID", "user", "roomID", "name", "arrive", "depart")
class UserProfileEntry(admin.ModelAdmin):
    list_display = ("user", "verified", "booking_mail_sent", "arrive", "depart", "street", "city", "reference_email")

admin.site.register(FormSubmit,AllEntryAdmin)
admin.site.register(ReferenceMail,AllEntryAdmin1)
admin.site.register(Room,RoomEntry)
admin.site.register(Booking,BookingEntry)
admin.site.register(UserProfile,UserProfileEntry)

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    ordering = ('-id',)

class BookinInLine(admin.StackedInline):
    model = Booking
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [ ProfileInline, BookinInLine,]
    ordering = ('-id', )
    fieldsets = (
            (None, {'fields': ('first_name','email', 'password')}),
    )

    def reference_verified(self, obj):
        try:
            return obj.userprofile.reference_verified
        except UserProfile.DoesNotExist:
            return ''
    reference_verified.Boolean = True
    def admin_verified(self, obj):
        try:
            return obj.userprofile.director_verified
        except UserProfile.DoesNotExist:
            return ''
    def verified(self, obj):
        try:
            return obj.userprofile.verified
        except UserProfile.DoesNotExist:
            return ''
    def applied_for_member(self, obj):
        try:
            return obj.userprofile.applied_for_member
        except UserProfile.DoesNotExist:
            return ''
    def is_member(self, obj):
        try:
            return obj.userprofile.is_member
        except UserProfile.DoesNotExist:
            return ''
    def room(self, obj):
        try:
            return obj.booking.roomID
        except Booking.DoesNotExist:
            return ''
    list_display =  ('first_name','id','email','reference_verified','admin_verified','verified','room','applied_for_member','is_member')
    list_filter =('userprofile__is_member',)

admin.site.unregister(User)
admin.site.register(User,UserProfileAdmin)
#admin.site.unregister(Group)
