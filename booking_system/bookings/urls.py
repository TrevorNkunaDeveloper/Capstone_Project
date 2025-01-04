from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('book/', views.booking_page, name='booking_page'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('reschedule/<int:booking_id>/', views.reschedule_booking, name='reschedule_booking'),
    path('payment/', views.payment_page, name='payment_page'),
]
