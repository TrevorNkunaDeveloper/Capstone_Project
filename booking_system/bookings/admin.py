"""
This module registers the Room, Booking, and UserProfile models with the Django admin interface
and defines custom admin configurations for each model.

Classes:
    RoomAdmin: Customizes the admin interface for Room objects by specifying fields
               to display, search, and filter.
               
    BookingAdmin: Customizes the admin interface for Booking objects by specifying fields
                  to display, search, and filter.

    UserProfileAdmin: Customizes the admin interface for UserProfile objects by specifying
                      fields to display.

Model Registrations:
    admin.site.register(Room, RoomAdmin): Registers the Room model with its custom admin class.
    admin.site.register(Booking, BookingAdmin): Registers the Booking model with its custom admin class.
    admin.site.register(UserProfile, UserProfileAdmin): Registers the UserProfile model with its custom admin class.
"""

from django.contrib import admin
from .models import Room, Booking, UserProfile

# Admin configuration for the Room model.
# This custom admin class specifies how Room objects are displayed in the admin interface.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'price_per_night')
    search_fields = ('name', 'room_type')
    list_filter = ('room_type',)

# Admin configuration for the Booking model.
# This custom admin class specifies how Booking objects are displayed in the admin interface.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'booking_date', 'nights', 'total_price')
    search_fields = ('user__username', 'room__name')
    list_filter = ('booking_date', 'created_at')

# Admin configuration for the UserProfile model.
# This custom admin class specifies how UserProfile objects are displayed in the admin interface.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')

# Register the models with their corresponding custom admin configurations.
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
