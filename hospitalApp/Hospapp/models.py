from django.db import models

# Create your models here.
# class RegisterDB (models.Model):
#     fName = models.CharField()
#     lName = models.CharField()



#     elif client != None:

#         # the list_database_names() method returns a list of strings
#         database_names = client.list_database_names()

#         print ("database_names() TYPE:", type(database_names))
#         print ("The client's list_database_names() method returned", len(database_names), "database names.")

#         # iterate over the list of database names
#         for db_num, db in enumerate(database_names):

#             # print the database name
#             print ("\nGetting collections for database:", db, "--", db_num)

#             # use the list_collection_names() method to return collection names
#             collection_names = client[db].list_collection_names()
#             print ("list_collection_names() TYPE:", type(database_names))
#             print ("The MongoDB database returned", len(collection_names), "collections.")

#             # iterate over the list of collection names
#             for col_num, col in enumerate(collection_names):
#                 print (col, "--", col_num)

#     else:
#         print ("The domain and port parameters passed to client's host is invalid")


# def find_document(collection, elements, multiple=False):
#     """ Function to retrieve single or multiple documents from a provided
#     Collection using a dictionary containing a document's elements.
#     """
#     if multiple:
#         results = collection.find(elements)
#         return [r for r in results]
#     else:
#         return collection.find(elements)

#  elif (actor == ''):
#         stud = []

#         tbl = "<tr><th>Id</th><th>First Name</th><th>Last Name</th><th>Sex</th><th>Mobile</th><th>CNIC</th><th>Email</th><th>Department</th><th>Doctor</th><th>Time</th><th>Date</th></tr>"
#         stud.append(tbl)

#         for y in BookApt.find():
#             id = "<tr><td>%s</td>"%y['id']
#             stud.append(id)
#             fname = "<td>%s</td>"%y['FirstName']
#             stud.append(fname)
#             lname = "<td>%s</td>"%y['LastName']
#             stud.append(lname)
#             sex = "<td>%s</td>"%y['sex']
#             stud.append(sex)
#             mob = "<td>%s</td>"%y['mobile']
#             stud.append(mob)
#             CNIC = "<td>%s</td>"%y['CNIC']
#             stud.append(CNIC)
#             email = "<td>%s</td>"%y['email']
#             stud.append(email)
#             Dept = "<td>%s</td>"%y['department']
#             stud.append(Dept)
#             doc = "<td>%s</td>"%y['doctor']
#             stud.append(doc)
#             time= "<td>%s</td>"%y['Time']
#             stud.append(time)
#             date = "<td>%s</td></tr>"%y['Date']
#             stud.append(date)
#         makefile_html(stud) 

#     elif (actor == "delete"):
#         for data in BookApt.find():
#             BookApt.delete_one(data)
# def makefile_html(stud):
#     contents = '''<!DOCTYPE HTML>
#     <html lang="en">
#     <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
#         integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous"/>
#     <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
#     <script src="js/bootstrap.js"></script>
#     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
#     <title>Bookings</title>
#     </head>
#     <body>
#     <h1> Booked Appointment List </h1>
#     <table >
#     %s
#     </table>
#     <br>
#     <form action="delete" method="POST">
#         Name: <input type="text" name="fname" />
#         <input type="button" value="submit"/>
#     </form>
#     </body>
#     </html>
#     '''%(stud)
#     save_path = '/Users/areeshamaqsood/Desktop/desktop/notes/SE/Project/hospitalApp/Hospapp/templates/Hospapp/'
#     filename = 'confirmed.html'

#     finalname = os.path.join(save_path,filename)
#     main(finalname,contents)

# def main(filename, contents):
#     output = open(filename,"w")
#     output.write(contents)
#     output.close()

#     # filename = 'file:///Users/areeshamaqsood/Desktop/desktop/notes/SE/Project/hospitalApp/Hospapp/templates/Hospapp/'+'confirmed.html'    
#     webbrowser.open(filename)