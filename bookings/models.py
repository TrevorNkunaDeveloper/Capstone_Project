"""
This module defines the models for the booking system, including rooms, bookings, and user profiles.

Classes:
    Room: Represents a room available for booking, including its type, price, and description.
    
    Booking: Represents a booking made by a user, including the room booked, booking date,
             duration (in nights), and total price. Also includes methods for calculating
             the total price and refunds.
             
    UserProfile: Represents additional information about a user, including a profile picture.

Methods:
    Room.__str__(): Returns a string representation of the room, including its name and type.
    
    Booking.save(): Overrides the default save method to automatically calculate the total price
                    based on the room price and number of nights.
                    
    Booking.calculate_refund(): Calculates the refund amount based on how many days in advance
                                the booking is cancelled.
                                
    Booking.__str__(): Returns a string representation of the booking.
    
    UserProfile.__str__(): Returns a string representation of the user profile.
"""
# Import Libraries 
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import date

# Represents a room available for booking.
class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
    ]

    name = models.CharField(max_length=50)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_room_type_display()})"

# Represents a booking made by a user.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateField()
    nights = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)
    refund_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.nights * self.room.price_per_night
        super().save(*args, **kwargs)

    def calculate_refund(self):
        days_before_booking = (self.booking_date - date.today()).days

        if days_before_booking >= 14:
            return self.total_price  # 100% refund
        elif days_before_booking >= 7:
            return self.total_price * Decimal('0.5')  # 50% refund
        else:
            return Decimal('0')  # No refund

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room.name}"

# Represents additional information about a user.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
