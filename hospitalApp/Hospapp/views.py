from abc import abstractproperty
import django
from django import template
import random
from datetime import datetime as dt
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import *
from django.template import loader
from .BL.hmsbl import newPatient as np , newBooking as nb, findpatient, admitpatient as ap, getbookings, savebookings, deleteBooking, dischargepatient as dis, getconfirmbookings, makeupdate, storecheckup
from .DB.hmsdb import find_document as fd
# Create your views here.
def homepage(request):
    return render(request,'Hospapp/index.html')

def doctorpage(request):
    return render(request,'Hospapp/doctor.html')

def receppage(request):
    return render(request,'Hospapp/receptionist.html')

def logout(request):
    return render(request,'Hospapp/login.html')

def login(request):
    if request.method=="POST":
        form = loginForm(request.POST)
        # print(form)
        if form.is_valid():
            password= form.cleaned_data["password"]
            username= form.cleaned_data["username"]
            if (username=="Doctor" and password=="Doc@123"):
                return render(request,"Hospapp/doctor.html",{"form":form})
            elif(username=="Receptionist" and password=="Recep@456"):
                return render(request,"Hospapp/receptionist.html",{"form":form})
            elif(username=="User" and password=="User@789"):
                return render(request,"Hospapp/user.html",{"form":form})
    else:
        form = loginForm()
    template=loader.get_template("Hospapp/login.html")
    return HttpResponse(template.render({"form":form},request))


def BookAppointment(request):
    
    if request.method == "POST":
        form = bookingForm(request.POST)
        
        if form.is_valid():
            FirstName= form.cleaned_data["FirstName"]
            LastName=form.cleaned_data["LastName"]
            sex=form.cleaned_data["sex"]
            email=form.cleaned_data["email"]  
            mobile=form.cleaned_data["mobile"]
            CNIC=form.cleaned_data["CNIC"]
            dept=form.cleaned_data["dept"]
            doc=form.cleaned_data["doc"]
            Date=form.cleaned_data["Date"]
            Time=form.cleaned_data["Time"]
            print("\n Appointment Booked:\n ",FirstName,LastName,sex,email,CNIC,mobile,dept,doc,Time,Date,"\n\n\n")
            nb(FirstName,LastName,sex,email,CNIC,mobile,dept,doc,Time,Date) 
    else: 
        form= bookingForm()
    template=loader.get_template("Hospapp/BookAppointment.html")
    return HttpResponse(template.render({"form":form},request))

def confirmAppointment(request):
    
    data = getbookings()
    print(type(data))
    print(data)
    return render(request, 'Hospapp/confirmAppointment.html', {'appointments': data,
                                                               'title': 'Confirmed Appointments'})

def confirm_appointment(request):
    
    print("\nComes here\n")
    if request.method == "POST":
        form = confirmApt(request.POST)

        if form.is_valid():

            FirstName = form.cleaned_data["FirstName"]
            LastName = form.cleaned_data["LastName"]
            sex = form.cleaned_data["sex"]
            CNIC = form.cleaned_data["CNIC"]
            mobile = form.cleaned_data["mobile"]   
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            Time = form.cleaned_data["Time"]
            doctor = form.cleaned_data["doctor"]
            department = form.cleaned_data["department"]
            print("\n Appointment Confirmed:\n ",FirstName,LastName,sex,email,CNIC,mobile,department,doctor,Time,date,"\n\n\n")
            # adding in confirmed appointments database
            savebookings(FirstName,LastName,sex,email,CNIC,mobile,department,doctor,Time,date)
            # deleting from booked appointment database
            deleteBooking(CNIC)

        else:
            print("Form not valid\n")
    else:
        form = confirmApt()

    template = loader.get_template("Hospapp/receptionist.html")
    return HttpResponse(template.render({"form": form}, request))

# def Checkup(request):
#     print("\n in checkup\n")
#     if request.method == "POST":
#         form = Check_up(request.POST)
#         print("\n outside is valid\n")
#         if form.is_valid():
#             print("\n is valid \n")
#             fName = form.cleaned_data["fName"]
#             lName = form.cleaned_data["lName"]
#             print("\nname entered\n", fName, lName)
#         else:
#             print("form not valid")
#     else:
#         form = Check_up()

#     template = loader.get_template("Hospapp/checkUp.html")
#     return HttpResponse(template.render({"form":form}, request))


def registerPatient(request):
    
    userid ="-"
    uid = dict()
    uid['userid']=userid
    # print("\n in register patient\n")
    if request.method == "POST":
        form = Register(request.POST)
        # print("\n outside is valid\n")
        if form.is_valid():
            # print("is valid\n")
            
            fName = form.cleaned_data["fName"]
            lName = form.cleaned_data["lName"]
            sex=form.cleaned_data["sex"]
            email=form.cleaned_data["email"]  
            mobile=form.cleaned_data["mobile"]
            CNIC=form.cleaned_data["CNIC"]
            address=form.cleaned_data["address"]
            uid['userid']= "User"
            print(uid['userid'])
            print("Patient Registered: \n", fName, lName,sex,mobile,email,CNIC,address,uid['userid'])
            np(fName,lName,sex,CNIC,mobile,email,address)
    else:
        form = Register()

    template = loader.get_template("Hospapp/register.html")
    return HttpResponse(template.render({"form":form}, request))

#opens the lift of booked appointments
def checkBookings(request):
    return render(request,'Hospapp/confirmed.html')

def confirmBooking(request):
    if request.method=="POST":
        pass

def admit_patient(request):

    # Variables initialized with none
    patientFirstName = "-"
    patientLastName = "-"
    patientSex = "-"
    patientCNIC = "-"
    patientContact = "-"
    patientEmail = "-"
    admissionDate = "-"
    admissionTime = "-"
    doc_name = "-"

    # Allocate a random ward no
    random.seed()
    wardNo = None

    patient_details = dict()
    patient_details['patientFirstName'] = patientFirstName
    patient_details['patientLastName'] = patientLastName
    patient_details['patientSex'] = patientSex
    patient_details['patientCNIC'] = patientCNIC
    patient_details['patientContact'] = patientContact
    patient_details['patientEmail'] = patientEmail
    patient_details['admissionDate'] = admissionDate
    patient_details['admissionTime'] = admissionTime
    patient_details['doc_name'] = doc_name
    patient_details['wardNo'] = wardNo
    
    list_doctors = ['Dr. Sajjad', 'Dr. Ijaz', 'Dr. Amna', 'Dr. Mazhar']
    random_ind = random.randint(0,3)

    now = dt.now()
    today = dt.today()
    # getdata = dict()

    # Fetch CNIC from form
    if request.method == "POST":
        form = admitPatient(request.POST)

        if form.is_valid():
            patientCNIC = form.cleaned_data["patientCNIC"]
            getdata = findpatient(patientCNIC)
            print(getdata)
            
            if getdata == 0:
                patient_details['patientFirstName'] = patientFirstName
                patient_details['patientLastName'] = patientLastName
                patient_details['patientSex'] = patientSex
                patient_details['patientCNIC'] = '-'
                patient_details['patientContact'] = patientContact
                patient_details['patientEmail'] = patientEmail
                patient_details['admissionDate'] = admissionDate
                patient_details['admissionTime'] = admissionTime
                patient_details['doc_name'] = doc_name
                patient_details['wardNo'] = wardNo
                
            else:
                
                wardNo = random.randint(5, 25)
                patient_details['patientFirstName'] = getdata['fName']
                patient_details['patientLastName'] = getdata['lName']
                patient_details['patientSex'] = getdata['sex']
                patient_details['patientCNIC'] = patientCNIC
                patient_details['patientContact'] = getdata['mobile']
                patient_details['patientEmail'] = getdata['email']
                patient_details['admissionDate'] = today.strftime("%m/%d/%y")
                patient_details['admissionTime'] = now.strftime("%H:%M:%S")
                patient_details['doc_name'] = list_doctors[random_ind]
                patient_details['wardNo'] = wardNo
                ap(getdata['fName'],getdata['lName'],getdata['sex'],patientCNIC,getdata['mobile'],getdata['email'],patient_details['admissionTime'],patient_details['admissionDate'],wardNo,patient_details['doc_name'])

        else:
            form = admitPatient()

    print("\n")
    print(patientCNIC)
    print("\n")

    return render(request, 'Hospapp/admit_patient.html', patient_details)

def discharge_patient(request):
    '''
    CNIC=""
    print("in discharge \n")
    if request.method == "POST":
        form = Discharge(request.POST)

        if form.is_valid():
            fName = form.cleaned_data["fName"]
            lName = form.cleaned_data["lName"]
            CNIC = form.cleaned_data["CNIC"]
            date = form.cleaned_data["date"]
            #print("Patient Discharged: \n", fName, lName,  CNIC, date)
            dis(fName, lName,  CNIC, date)
            #fd(CNIC)

    else:
        form = Discharge()

    request.session['CNIC'] = CNIC
    print(CNIC)
    '''

    #mydoc = dict()
    #mydoc = {"CNIC" : CNIC}
    return render(request, 'Hospapp/discharge.html')

    #template = loader.get_template("Hospital/discharge.html")
    #return HttpResponse(template.render({"form": form}, request))


def pages(request):
    CNIC = ""
    print("in discharge \n")
    if request.method == "POST":
        form = Discharge(request.POST)

        if form.is_valid():
            #fName = form.cleaned_data["fName"]
            #lName = form.cleaned_data["lName"]
            CNIC = form.cleaned_data["CNIC"]
            print("Patient Discharged: \n",  CNIC)

            #fd(CNIC)
    else:
        form = Discharge()

    print("new page")
    print(CNIC)
    mydoc = {}
    mydoc = fd(CNIC)

    if mydoc == 0:
        template = loader.get_template("Hospapp/discharge.html")
        return HttpResponse(template.render({"form": form}, request))
    else:
        dis(CNIC)
        return render(request, 'Hospapp/admit_dis.html', {'mydoc': mydoc})


# checkUp
def listAllAppointments(request):
    # Search the database for all the appointments
    # data = {
    #     'appointments': Appointment.objects.all(),
    #     'title': 'Confirmed Appointments'
    # }
    data = getconfirmbookings()
    print(type(data))
    print(data)
    return render(request, 'Hospapp/listAllAppointments.html', {'appointments': data,
                                                               'title': 'Confirmed Appointments'})
    # return render(request, 'HMS/listAllAppointments.html', data)

def start_checkup(request):

    # A session here is not necessary but exits only for
    # learning purpose

    if request.method == "POST":
        form = startCheckUp(request.POST)

        if form.is_valid():

            patientFirstName = form.cleaned_data["FirstName"]
            patientLastName = form.cleaned_data["LastName"]
            patientSex = form.cleaned_data["sex"]
            appointment_date = form.cleaned_data["Date"]
            appointment_time = form.cleaned_data["Time"]
            patientCNIC= form.cleaned_data["CNIC"]

            request.session['FirstName'] = patientFirstName
            request.session['LastName'] = patientLastName
            request.session['sex'] = patientSex
            request.session['Date'] = appointment_date
            request.session['Time'] = appointment_time
            request.session['CNIC'] = patientCNIC

        else:
            print("Form not valid\n")
    else:
        form = startCheckUp()

    # template = loader.get_template("HMS/checkup_new.html")
    # return HttpResponse(template.render({"form": form}, request))

    patientFirstName = request.session['FirstName']
    patientLastName = request.session['LastName']
    patientSex = request.session['sex']
    appointment_date = request.session['Date']
    appointment_time = request.session['Time']
    patientCNIC = request.session['CNIC']

    print('\n')
    print(patientFirstName)
    print(patientLastName)
    print(patientSex)
    print(appointment_date)
    print(appointment_time)
    print(patientCNIC)
    print('\n')

    patient_details = dict()
    patient_details['FirstName'] = patientFirstName
    patient_details['LastName'] = patientLastName
    patient_details['sex'] = patientSex
    patient_details['Date'] = appointment_date
    patient_details['Time'] = appointment_time
    patient_details['CNIC'] = patientCNIC

    storecheckup(patientFirstName,patientLastName,patientSex,patientCNIC,appointment_date,appointment_time,"-","-")

    return render(request, 'Hospapp/checkup_new.html', patient_details)


def Diagnose(request):
    # print("\n in diagnosis\n")
    if request.method == "POST":
        form = Diagnosis(request.POST)

        # print("\n diagnosis is valid\n")
        if form.is_valid():
            # print("\n is valid\n")
            diagnosis_box = form.cleaned_data["diagnosis_box"]
            print("\ndiagnosis entered\n", diagnosis_box)
        else:
            print("form not valid")
    else:
        form = Diagnosis()

    template = loader.get_template("Hospapp/checkup_new.html")
    return HttpResponse(template.render({"form": form}, request))


def Prescribe_Medicine(request):
    # print("\n in Medicine\n")
    if request.method == "POST":
        form = Meds(request.POST)

        # print("\n prescribe medicine\n")
        if form.is_valid():
            # print("\n is valid\n")
            medicine = form.cleaned_data["medicine"]
            description = form.cleaned_data["description"]
            dosage = form.cleaned_data["dosage"]
            print("\nprescription entered\n", medicine, dosage, description)
        else:
            print("form not valid")
    else:
        form = Meds()

    template = loader.get_template("Hospapp/checkup_new.html")
    return HttpResponse(template.render({"form": form}, request))