from ..DB.hmsdb import dbconnection

def newPatient(fName,lName,sex,CNIC,mobile,email,address):
    recepDetails = dbconnection("Receptionist","-")

    doc = { 
        "id": str(recepDetails[1]), 
        "fName": fName,
        "lName": lName,
        "sex": sex,
        "CNIC": CNIC,
        "mobile": mobile,
        "email": email,
        "address": address
    }

    recepDetails[0].insert_one(doc)

def newBooking(FirstName,LastName,sex,email,CNIC,mobile,dept,doc,Time,Date):
    bookDetails = dbconnection("User","-")

    document = { 
        "id": str(bookDetails[1]), 
        "FirstName": FirstName,
        "LastName": LastName,
        "sex": sex,
        "CNIC": CNIC,
        "mobile": mobile,
        "email": email,
        "department": dept,
        "doctor": doc,
        "Time": Time,
        "Date": Date
    }

    bookDetails[0].insert_one(document)


def findpatient(CNIC):
    print("Going to hmsdb.py \n")
    print(CNIC)
    data = dbconnection("findpatient", CNIC)
    return data


def admitpatient(fName,lName,sex,CNIC,mobile,email,time,date,ward,doctor):
    recepDetails = dbconnection("saveadmit","-")

    doc = { 
        "id": str(recepDetails[1]), 
        "fName": fName,
        "lName": lName,
        "sex": sex,
        "CNIC": CNIC,
        "mobile": mobile,
        "email": email,
        "time": time,
        "date": date,
        "ward": ward,
        "doctor": doctor
    }

    recepDetails[0].insert_one(doc)

#for getting the list of booked appointments in confirmed
def getbookings():
    getdict = dbconnection("getbookings","-")
    return getdict

#saved appointment in confirmed appointment 
def savebookings(FirstName,LastName,sex,email,CNIC,mobile,dept,doc,Time,Date):
    bookDetails = dbconnection("confirmBooking","-")

    document = { 
        "id": str(bookDetails[1]), 
        "FirstName": FirstName,
        "LastName": LastName,
        "sex": sex,
        "CNIC": CNIC,
        "mobile": mobile,
        "email": email,
        "department": dept,
        "doctor": doc,
        "Time": Time,
        "Date": Date
    }

    bookDetails[0].insert_one(document)

#deletes confirms appointment from booked appointments lists
def deleteBooking(CNIC):
    print("deleting from book appintment...")
    dbconnection("deleteBooking",CNIC)

def deleteAll():
    dbconnection("deleteall","-")

def dischargepatient(CNIC):
    Discharge_Details = dbconnection("discharge","-")
    doc = {
        "CNIC": CNIC
    }
    Discharge_Details[0].insert_one(doc)

# getting list of confirmed appointments to start the checkup
def getconfirmbookings():
    getdict = dbconnection("confirmedapt","-")
    return getdict

def makeupdate(mobile):
    dbconnection("adding",mobile)
    print("bl: Added in already created document \n")
