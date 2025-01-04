"""
This module defines Django ModelForms for user registration and booking management.

Classes:
    UserRegistrationForm: A form for registering new users, extending the built-in
                          Django User model. Includes custom password confirmation
                          validation and applies Bootstrap styling to form fields.
                          
    BookingForm: A form for creating and managing bookings, extending the Booking model.
                 Includes fields for room selection, booking date, and number of nights,
                 with Bootstrap-styled widgets for a consistent user interface.
"""

from django import forms
from django.contrib.auth.models import User
from .models import Booking

# Form for user registration.
# Inherits from forms.ModelForm to handle user registration fields.
class UserRegistrationForm(forms.ModelForm):
    """
    A form for registering new users, extending the built-in Django User model.
    
    Attributes:
        password (CharField): A password input field styled with Bootstrap.
        password_confirm (CharField): A password confirmation input field styled with Bootstrap.
    
    Meta:
        model (User): Specifies that this form is based on the built-in Django User model.
        fields (list): Specifies the fields to be displayed in the form (username, email, password).
        widgets (dict): Applies Bootstrap styling to the username and email fields.
    
    Methods:
        clean_password_confirm(): Validates that the password and password confirmation match.
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password_confirm(self):
        """
        Validates that the password and password confirmation match.
        
        Returns:
            str: The confirmed password if it matches the original password.
        
        Raises:
            forms.ValidationError: If the passwords do not match.
        """
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return password_confirm

# Form for making a booking.
# Inherits from forms.ModelForm to handle booking-related fields.
class BookingForm(forms.ModelForm):
    """
    A form for creating and managing bookings, extending the Booking model.
    
    Meta:
        model (Booking): Specifies that this form is based on the Booking model.
        fields (list): Specifies the fields to be displayed in the form (room, booking_date, nights).
        widgets (dict): Applies Bootstrap styling to the form fields (room, booking_date, nights).
    """
    class Meta:
        model = Booking
        fields = ['room', 'booking_date', 'nights']
        widgets = {
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nights': forms.NumberInput(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
        }