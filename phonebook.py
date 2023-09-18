import mysql.connector

print("1.Add new contact")
print("2.view all contacts")
print("3.delete contact")
print("4.edit contact")
selected_option = int(input("select option : "))

if selected_option == 1:
    # read details from the user
    name = input("Enter name : ")
    phone = input("Enter contact number : ")

    # connect to database
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Gshock@123", database="phonebook"
    )
    # save to database
    mycursor = mydb.cursor()
    insert_sql = "insert into contacts(name,phone) values(%s,%s)"
    data = (name, phone)
    mycursor.execute(insert_sql, data)
    mydb.commit()


elif selected_option == 2:
    # connect to database
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Gshock@123", database="phonebook"
    )
    mycursor = mydb.cursor()

    # read all contacts from database
    mycursor.execute("select * from contacts")
    contacts = mycursor.fetchall()

    # show contactsm
    for contact in contacts:
        print(contact[0], ".", contact[1], ":", contact[2])

elif selected_option == 3:
    # read the contact id to delete
    id = int(input("Enter contact id to delete : "))

    # connect to database
    mydb = mysql.connector.connect(
        user="root", host="localhost", password="Gshock@123", database="phonebook"
    )
    mycursor = mydb.cursor()

    # create the query
    delete_query = "DELETE FROM contacts WHERE id=%s"

    # excecute the query
    data = (id,)
    mycursor.execute(delete_query, data)
    mydb.commit()
