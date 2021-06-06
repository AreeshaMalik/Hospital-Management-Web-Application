from django import forms 
# from phonenumber_field.formfields import PhoneNumberField

class loginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class bookingForm(forms.Form):
    FirstName=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    LastName=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    sex=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'input'}))    
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    CNIC=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    dept=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    doc=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    Date=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    Time=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class startCheckUp(forms.Form):
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    LastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    sex = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    Date = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    Time = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    CNIC = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

class Diagnosis(forms.Form):
    diagnosis_box = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

class Meds(forms.Form):
    medicine = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    dosage = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

class Register(forms.Form):
    fName=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    lName=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    sex=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'input'}))    
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    CNIC=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'input'})) 

class admitPatient(forms.Form):
    patientCNIC = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    
class confirmApt(forms.Form):
    FirstName=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    LastName=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    sex=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    CNIC=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'input'}))
    date=forms.CharField(widget=forms.TextInput(attrs={'class':'input'})) 
    Time=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    doctor=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))    
    department=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class Discharge(forms.Form):
    #fName = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    #lName = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    CNIC = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

class getPres(forms.Form):
    CNIC = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    Date = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))


class getReport(forms.Form):
    CNIC = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))