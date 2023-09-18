import mysql.connector
import sys

# connect to database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Gshock@123", database="phonebook"
)
mycursor = mydb.cursor()


print("1.Add new contact")
print("2.view all contacts")
print("3.delete contact")
print("4.edit contact")
selected_option = int(input("select option : "))

if selected_option == 1:
    # read details from the user
    name = input("Enter name : ")
    phone = input("Enter contact number : ")

    # validate phone number
    # 1. phone number should be 10 digits
    # 2. phone number only contain digits
    # 3. phone number should always start with 0
    if len(phone)!= 10:
        print("phone number should be 10 digits")
        sys.exit(0)
    if not phone.isdigit():
        print("phone number should only contain digits")
        sys.exit(0)
    if not phone.startswith("0"):
        print("phone number always should starts with o")
        sys.exit(0)
        
    # save to database
    insert_sql = "insert into contacts(name,phone) values(%s,%s)"
    data = (name, phone)
    mycursor.execute(insert_sql, data)
    mydb.commit()


elif selected_option == 2:
    # read all contacts from database
    mycursor.execute("select * from contacts")
    contacts = mycursor.fetchall()

    # show contactsm
    for contact in contacts:
        print(contact[0], ".", contact[1], ":", contact[2])

elif selected_option == 3:
    # read the contact id to delete
    id = int(input("Enter contact id to delete : "))

    # create the query
    delete_query = "DELETE FROM contacts WHERE id=%s"

    # excecute the query
    data = (id,)
    mycursor.execute(delete_query, data)
    mydb.commit()

elif selected_option == 4:
    # read contact id to be edited from the user
    id = int(input("enter contact id to be edited : "))

    # read the new phone number to be modified
    new_number = input("Enter new phone number : ")

     # validate phone number
    # 1. phone number should be 10 digits
    # 2. phone number only contain digits
    # 3. phone number should always start with 0
    if len(new_number)!= 10:
        print("phone number should be 10 digits")
        sys.exit(0)
    if not new_number.isdigit():
        print("phone number should only contain digits")
        sys.exit(0)
    if not new_number.startswith("0"):
        print("phone number always should starts with o")
        sys.exit(0)
    
    # build update query
    update_query = "update contacts set phone=%s where id = %s"

    # execute update
    data = (new_number, id)
    mycursor.execute(update_query, data)
    mydb.commit()
else:
    print("wrong input")