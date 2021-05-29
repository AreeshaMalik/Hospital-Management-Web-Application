import pymongo
import webbrowser

client = pymongo.MongoClient("mongodb+srv://areesha:Areesha123@se.0nmlc.mongodb.net/HMS?retryWrites=true&w=majority")
mydb = client["HMS"]
mycol = mydb["Booked Appointments"]

stud = []

tbl = "<tr><td>First Name</td><td>Last Name</td><td>Sex</td><td>Mobile</td></tr>"
stud.append(tbl)

for y in mycol.find():
    a = "<tr><td>%s</td>"%y['FirstName']
    stud.append(a)
    b = "<td>%s</td>"%y['LastName']
    stud.append(b)
    c = "<td>%s</td></tr>"%y['sex']
    stud.append(c)
    d = "<td>%s</td></tr>"%y['mobile']
    stud.append(d)

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(stud)

filename = 'comfirmed.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)
filename = 'file:///Users/areeshamaqsood/Desktop/desktop/notes/SE/Project/hospitalApp/Hospapp/templates/Hospapp/'+'confirmed.html'    
webbrowser.open(filename)