import pymongo
import django
# import webbrowser 
# import os.path

def dbconnection(actor,check):
    client = pymongo.MongoClient("mongodb+srv://areesha:Areesha123@se.0nmlc.mongodb.net/HMS?retryWrites=true&w=majority")
    db = client['HMS']

    Register = db['Registered']
    BookApt  = db['Booked Appointments']
    RegList = Register.count()
    Booklist = BookApt.count()
    Admit  = db["Admit Patients"]
    Admitlist = Admit.count()
    Confirmed = db['Confirmed Appointments']
    Confirmedlist = Confirmed.count()
    Discharge = db["Discharge Patients"]
    Dischargelist = Discharge.count()


    samplelist = list()
    samplebooked = list()
    sampleadmit = list()
    sampleconfirm = list()
    sample_discharge = list()

    updt = db['CheckUpdate']
    uplist = updt.count()

    if (actor == "Receptionist"):
        samplelist.append(Register)
        samplelist.append(RegList)

        return samplelist

    elif (actor == "User"):
        samplebooked.append(BookApt)
        samplebooked.append(Booklist)

        return samplebooked

    elif (actor == "findpatient"):
        print("Printing the database \n")
        for data in Register.find({"CNIC": check}):
            print(data)
        try:
            return data
        except:
            return 0

    elif (actor == "saveadmit"):
        sampleadmit.append(Admit)
        sampleadmit.append(Admitlist)

        return sampleadmit
    
    elif (actor ==  "getbookings"):
        getdict = dict()
        a = 0
        for data in BookApt.find():
            # return data
            getdict[a] = data
            a = a + 1
        return getdict

    elif (actor == "confirmBooking"):
        sampleconfirm.append(Confirmed)
        sampleconfirm.append(Confirmedlist)

        return sampleconfirm

    elif (actor == "deleteBooking"):
        BookApt.delete_one({"CNIC":check})
        print(check,"deleted!")
    
    elif actor == "discharge":
        sample_discharge.append(Discharge)
        sample_discharge.append(Dischargelist)
        return sample_discharge
    
    elif actor == "confirmedapt":
        getdict = dict()
        a = 0
        for data in Confirmed.find():
            getdict[a] = data
            a = a + 1
        return getdict
    
    elif actor == "adding":
        updt.update({"name" :"Areesha" },{"$set":{"mobile":check}})
        print("db: updated \n")

    elif (actor == "deleteall"):
        Register.delete_many()

def find_document(CNIC):
    client = pymongo.MongoClient("mongodb+srv://areesha:Areesha123@se.0nmlc.mongodb.net/HMS?retryWrites=true&w=majority")
    db = client['HMS']
    Admit  = db["Admit Patients"]
    myquery = {'CNIC': CNIC}
    mydoc = Admit.find(myquery)
    newdoc={}
    if mydoc.count() == 0:
        return 0
    else:
        for key, value in mydoc.next().items():
            newdoc[key] = value
        return newdoc


def saveCheckup(FirstName,LastName,sex,CNIC,Date,Time):
    client = pymongo.MongoClient("mongodb+srv://areesha:Areesha123@se.0nmlc.mongodb.net/HMS?retryWrites=true&w=majority")
    db = client['HMS']

    checkup = db["CheckUp"]
    checklist = checkup.count()
    samplecheckup = list()

    
