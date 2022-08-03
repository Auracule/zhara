from django.contrib import admin
from . models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','img', 'name','slug', 'min_price','description_c']
    list_editable = ['img']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'category','slug','available','category_id', 'name_r', 'img_r', 'price_r', 'adult_no', 'kids_no','description', 'economy', 'family', 'business', 'royals']
    list_editable = ['description', 'economy', 'family', 'business', 'royals']
    prepopulated_fields = {'slug': ('name_r',)}

admin.site.register(Room, RoomAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display =['id', 'user', 'room', 'price_b', 'check_in', 'check_out', 'no_days', 'amount', 'paid']
admin.site.register(Booking, BookingAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gallery', 'slide1', 'slide2', 'slide3']
admin.site.register(Gallery, GalleryAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email',  'message', 'add_note', 'status', 'dated', 'attended']
admin.site.register(Contact, ContactAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'phone', 'address', 'state', 'pix']
admin.site.register(Profile, ProfileAdmin)

