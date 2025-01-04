"""
This module defines the views for the booking system, handling user interactions such as 
home page display, booking creation, user registration, profile management, and booking 
cancellation or rescheduling.

Views:
    home_page(request): Renders the home page.
    booking_page(request): Handles room booking creation.
    signup(request): Handles user registration.
    long_running_task(): Simulates a long-running task.
    profile(request): Displays the user's profile with booking history.
    custom_logout(request): Logs the user out and redirects to the home page.
    cancel_booking(request, booking_id): Cancels a booking and processes the refund.
    reschedule_booking(request, booking_id): Allows a user to reschedule an existing booking.
    payment_page(request): Displays a payment form and handles payment submission.
"""
# Import Libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
import threading
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import date

# View to render the home page.
def home_page(request):
    return render(request, 'bookings/home.html')

# View to handle room booking.
@login_required
def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_page')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking.html', {'form': form})

# View to handle user registration.
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def long_running_task():
    # Simulate a long-running task
    import time
    time.sleep(5)
    print("Task Complete")

# View to handle the user's profile.
@login_required
def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been confirmed!')
            return redirect('profile')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking.html', {'form': form})

# View to display the user's profile.
@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/profile.html', {'bookings': bookings})

# View to log out the user.
def custom_logout(request):
    logout(request)
    return redirect('home_page')

# View to cancel a booking.
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.is_cancelled:
        messages.info(request, "This booking has already been cancelled.")
        return redirect('profile')

    refund = booking.calculate_refund()
    booking.is_cancelled = True
    booking.refund_amount = refund
    booking.save()

    messages.success(request, f"Booking cancelled. Refund Amount: R{refund:.2f}")
    return redirect('profile')

# View to reschedule a booking.
def reschedule_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        new_booking_date = request.POST.get('new_booking_date')
        if new_booking_date:
            refund = booking.calculate_refund()
            booking.booking_date = new_booking_date
            booking.refund_amount = refund
            booking.save()
            messages.success(request, f"Booking rescheduled to {new_booking_date}. Refund Adjustment: R{refund:.2f}")
            return redirect('profile')

    return render(request, 'bookings/reschedule_booking.html', {'booking': booking})

@login_required
def payment_page(request):

    if request.method == 'POST':
        # Simulate payment processing (in a real-world scenario, integrate a payment gateway here)
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # For now, assume the payment is always successful
        messages.success(request, 'Payment successful! Thank you for your booking.')
        return redirect('profile')
    
    return render(request, 'bookings/payment.html')