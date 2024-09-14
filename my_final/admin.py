from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from .models import BloodGroup, District, UserExtend, RequestBlood, UserExtend2

class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserExtendAdmin(admin.ModelAdmin):
    list_display = ('donor', 'date_of_birth', 'phone', 'address', 'district', 'blood_group', 'gender', 'ready_to_donate')
    list_filter = ('district', 'blood_group', 'gender', 'ready_to_donate')

class RequestBloodAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'donation_location', 'district', 'blood_group', 'date_of_donation', 'pin_code')
    list_filter = ('district', 'blood_group', 'date_of_donation')

class UserExtend2Admin(admin.ModelAdmin):
    list_display = ('patient','date_of_birth', 'phone', 'address', 'district', 'blood_group', 'gender', 'need_donation')
    list_filter = ( 'district', 'blood_group', 'gender', 'need_donation')

# Register your models with the admin site
admin.site.register(BloodGroup, BloodGroupAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(UserExtend, UserExtendAdmin)
admin.site.register(RequestBlood, RequestBloodAdmin)
admin.site.register(UserExtend2, UserExtend2Admin)