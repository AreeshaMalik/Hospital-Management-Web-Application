from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('doctor', views.doctorpage, name='doctor'),
    path('bookapt', views.BookAppointment, name='bookapt'),
    path('checkUp', views.Checkup, name='checkUp'),
    path('register',views.registerPatient, name='register'),
    path('receptionist',views.receppage,name='receptionist'),
    path('confirmed', views.confirmAppointment, name='confirmAppointment'),
    path('aptConfirmation', views.confirm_appointment, name='aptConfirmation'),
    path('admit_patient', views.admit_patient, name='admit_patient'),
    path('discharge', views.discharge_patient, name = 'discharge'),
    path('thePages', views.pages, name = 'thePages'),
    # path('delete',views.confirmBooking,name='delete'),
]