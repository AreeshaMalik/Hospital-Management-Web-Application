from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('doctor', views.doctorpage, name='doctor'),
    path('bookapt', views.BookAppointment, name='bookapt'),
    # path('checkUp', views.Checkup, name='checkUp'),
    path('register',views.registerPatient, name='register'),
    path('receptionist',views.receppage,name='receptionist'),
    path('confirmed', views.confirmAppointment, name='confirmAppointment'),
    path('aptConfirmation', views.confirm_appointment, name='aptConfirmation'),
    path('admit_patient', views.admit_patient, name='admit_patient'),
    path('discharge', views.discharge_patient, name = 'discharge'),
    path('thePages', views.pages, name = 'thePages'),
    # path('delete',views.confirmBooking,name='delete'),
    path('listAllAppointments', views.listAllAppointments, name='listAllAppointments'),
    path('startCheckUp', views.start_checkup, name='startCheckUp'),
    path('Diagnosis', views.Diagnose, name='Diagnosis'),
    path('Prescribe_Medicine', views.Prescribe_Medicine, name='Prescription'),
    path('getPrescription', views.getPrescription, name='getPrescription'),
    path('getReport', views.get_report, name='getReport'),
]