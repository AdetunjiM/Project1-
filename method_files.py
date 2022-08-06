import mysql.connector
import mysql_config as c
from class_files import admin,customer,computer,orders
import re
import logging

try:
    cnx = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database="Project_1")
    cursor = cnx.cursor()
except mysql.connector.Error as mce:
    print(mce.msg)

except Exception as e:
    print("ERROR:Exiting the program")

logging.basicConfig(filename="citizencomputerstore.log",level=logging.DEBUG,format='%(asctime)s :: %(message)s')

def insert_records():
    logging.basicConfig(filename="citizencomputerstore.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    restart = True
    logging.info("Logging into the web")
    while restart :
        print("\n*****---WELCOME TO CITIZENS COMPUTER PORTAL---****** :")
        print("\t1) ADMIN Log In\n")
        print("\t2) Customer Log In\n")
        print("\t3) Quit\n")

        valid = False
        while not valid:
            try:
                input_type = int(input(" Enter Option >>>>"))
                valid= True
            except:
                print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")
                logging.info("User Inputs Invalid selection ")
        """if input_type not in ["1","2","3","4"]:
            print("Invalid Selection \n")"""

        if input_type ==1:
            print("***ADMIN LOG IN PORTAL***\n")
            admin_ops()
        elif input_type ==2:
            print("***CUSTOMER LOG IN PORTAL***\n")
            customer_ops()
        elif input_type ==3:
            print("***Quiting the program ..........<><><>***\n")
            logging.info("User Quit the Program ")
            restart = False
        else:
            print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]\nRestarting The Store>>>>>>>.........")
            logging.info("Invalid input was entered ")


def admin_ops():
    print("****LOG INTO THE ADMIN PORTAL****")
    restart = True
    while restart == True:
        while True:
            try:
                name =str(input("Enter ADMIN name >"))
                if re.search("[a-zA-Z]",name):
                    break
                else:
                    raise ValueError
                    print("\nInvalid name format")
            except ValueError as ve :
                print("Invalid name format.     NAME MUST BE A STRING :")
            else:
                break

        valid = False
        while not valid:
            try:
                passw =int(input("enter admin  passcode"))
                valid = True
            except:
                print("Invalid Input. PASSCODE must be an Integer : [1 , 2 , 3 , 4]")

        add= admin(name,passw)
        query_admin = f"SELECT * FROM admin where name ='{add.name}' and passcode ={add.passcode}"
        cursor.execute(query_admin)
        record = cursor.fetchone()
        #if passw == record[2] and name == record[1]:
        if record != None:
            print(f"\nADMIN Log in successful .......\nWELCOME {add.name}")
            logging.info("Successfully Loged Into The ADMIN portal")

            restart = True
            while restart == True:
                print(f"\nSELECT OPTION [1 , 2 , 3 , 4]")
                print("\t1) Add Records ")
                print("\t2) View  Records ")
                print("\t3) Update Existing Records ")
                print("\t4) Delete Existing Records ")
                print("\t5) quit ")

                valid = False
                while not valid:
                    try:
                        select = int(input(f"\nEnter Option: >>>>>>>>>>\n" ))
                        valid = True
                    except:
                        print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 5]")

                if select ==1:
                    print("Welcome to the Admin ADD RECORDS section\n Select Record To Add: ")
                    print("\t1) Add New ADMIN ")
                    print("\t2) Add New Customer ")
                    print("\t3) Add New Computer to Inventory  ")
                    print("\t4) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the ADD RECORDS section {add.name} \n>>>>>"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        add_new_admin()
                        restart=True
                    elif select ==2:
                        add_new_customer()
                        restart=True
                    elif select ==3:
                        add_new_computer()
                        restart = True
                    elif select ==4:
                        print("***Quiting the ADD RECORDS SECTION ..........<><><>***\n")
                        restart = False
                        break
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                        restart = True
                elif select == 2:
                    print("Welcome to the Admin VIEW RECORDS section\n Select Record To Add: ")
                    print("\t1) View Existing ADMIN accounts")
                    print("\t2) View Existing Customers")
                    print("\t3) View All Computers in Inventory")
                    print("\t4) View ONE Customer Orders")
                    print("\t5) View All Placed Orders")
                    print("\t6) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the VIEW RECORDS section {add.name}"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        view_all_Admin()
                    elif select == 2:
                        view_all_customers()
                    elif select == 3:
                        view_all_computers()
                    elif select == 4:
                        view_customer_orders()
                    elif select == 5:
                        view_all_orders()
                    elif select == 6:
                        print("***Quiting the VIEW RECORDS SECTION ..........<><><>***\n")
                        restart= False
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4 , 5 , 6]")
                elif select ==3:
                    print("Welcome to the Admin UPDATE RECORDS section\n Select Record To Add: ")
                    print("\t1) Modify Existing ADMIN Details")
                    print("\t2) Modify Existing Customers Details")
                    print("\t3) Modify Computers in Inventory")
                    print("\t4) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the MODIFY RECORDS section {add.name}"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        modify_admin()
                    elif select == 2:
                        modify_customer_records()
                    elif select == 3:
                        modify_computer()
                    elif select == 4:
                        print("***Quiting the UPDATE RECORDS SECTION ..........<><><>***\n")
                        restart = False
                        break
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                elif select ==4:
                    print("Welcome to the Admin DELETE RECORDS section\nSelect Record To DELETE: \n")
                    print("\t1) Delete Existing ADMIN Accounts")
                    print("\t2) Delete Existing Customers Accounts")
                    print("\t3) Delete Computers in Inventory")
                    print("\t4) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the DELETE RECORDS section {add.name}"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")
                    if select == 1:
                        delete_admin()
                    elif select == 2:
                        delete_customer_records()
                    elif select == 3:
                        delete_computer()
                    elif select == 4:
                        print("***Quiting the UPDATE RECORDS SECTION ..........<><><>***\n")
                        restart= False
                        break
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                        #call delete options  here
                elif select == 5:
                    print("***Quiting the ADMIN SECTION ..........<><><>***\n")
                    restart = False
                    break
                else:
                    print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                    logging.info("Invalid input was entered ")
                    restart = True

        else :
            print(f"\nUnregistered Admin:Unauthorised access to the ADMIN Portal \nExiting To HOME.............")
            logging.info("Unauthorised Login Attempt was Declined ")
            break
def customer_ops():
    while True:
        print("\t1) Existing Customer Log in")
        print("\t2) New Customer Log in")
        print("\t3) Quit")

        valid = False
        while not valid:
            try:
                input_type = int(input("Enter Option >>>>"))
                valid = True
            except:
                print("Invalid Input. Enter Input : [1 , 2 , 3 ]")


        if input_type ==1:
            print(f"Welcome Back Customer . Enter Log In details below:  \n")
            while True:
                try:
                    name = str(input(f"Registered Customer NAME >>>>>>\n"))
                    if re.search("[a-zA-Z]",name):
                        break
                    else:
                        raise  ValueError
                except ValueError as ve :
                    print("invalid name format :    NAME MUST BE A STRING:")
                else:
                    break


            valid = False
            while not valid:
                try:
                    custID = int(input("Registered Customer ID >>>>>>\n"))
                    valid = True
                except:
                    print("Invalid input Enter ")

            query_customer_login = f"SELECT  * FROM  customers WHERE name ='{name}' AND customerID = {custID};"
            #cursor.execute(query_customer_login)

            cursor.execute(query_customer_login)
            record = cursor.fetchone()
            # if passw == record[2] and name == record[1]:
            if record != None:
                logging.info("successful log into customer portal")
                print("Customer Log in successful....\n")
                print("\t1) Place an Order")
                print("\t2) View all orders")
                print("\t3) Quit")

                valid = False
                while not valid:
                    try:
                        input_type = int(input("Make Selection >>>>"))
                        valid = True
                    except:
                        print("Invalid input Enter ")
                if input_type == 1:
                    add_new_order()
                elif input_type == 2:
                    view_customer_orders()
                elif input_type == 3:
                    print("***Quiting the CUSTOMERS SECTION ..........<><><>***\n")
                    break
                    print(" log in")
            else:
                print("Unsuccessful Log in Attempt: Wrong Details Entered ")

        elif input_type == 2:
            print("New Customer Account Creation Page ")
            add_new_customer()

        elif input_type == 3:
            print("Quiting The Program")
            break
        else:
            print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]\n")
            logging.info("Invalid input was entered ")

"""********         FUNCTIONS ARE LISTED BELOW      *********"""

"""*******ADD RECORDS FUNCTIONS*******"""
def add_new_admin():
    valid = False
    while not valid:
        try:
            enter = (input("Enter master Admin password >>>>:\n"))

            valid = True
        except:
            print("Invalid Input. Enter an Integer ")

    cursor.execute(f"SELECT * FROM  masteradmin")
    for value in cursor:
        confirmPasword = value[3]

    while enter == confirmPasword:
        print("Successful log in ")
        logging.info("Master Admin account logged in  ")

        print(f"\nAdding a new Admin.........Enter Admin NAME: \n")
        while True:
            try:
                name = str(input(f">>>>>>>"))
                if re.search("[a-zA-Z]", name):
                    break
                else:
                    raise ValueError
                    print(f"\n Invalid name Format ")
            except ValueError as ve:
                print("Invalid Name Format .    NAME MUST BE A STRING :")

        valid = False
        while not valid:
            try:
                passcode = int(input("Enter New Admin Passcode: >>>\n"))
                valid = True
            except:
                print("Invalid Input. PASSCODE must be an Integer \n")

        new_admin = admin(name, passcode)
        query_add_new_admin = f"INSERT INTO admin (name,passcode)VALUES ('{new_admin.name}',{new_admin.passcode}) "

        cursor.execute(query_add_new_admin)
        cnx.commit()
        logging.info("a new admin account was created")
        print(f"A new Admin was added \nName: {name} \nPasscode: {passcode}")
        break


    else:
        print("Incorrect login ")

def add_new_order():

    A = "SELECT * FROM computer"
    cursor.execute(A)
    print("****COMPUTER INVENTORY ****\n")

    for record in cursor:
        print(record)
        new_order=orders(record[1],record[2],record[3],record[4],record[5])
    valid = False
    while not valid:
        try:
            selection = int(input("Enter ID of computer to Purchase: >>>\n"))
            valid = True
        except:
            print("Invalid Input. Computer ID  must be an Integer ")

    valid = False
    while not valid:
        try:
            custID = int(input("Confirm your customer ID  :>>>\n"))
            valid = True
        except:
            print("Invalid Input. Customer ID must be an Integer ")

    B = f"SELECT * FROM computer where computerID = {selection}"
    cursor.execute(B)
    for value in cursor:
        brand = value[1]
        model = value[2]
        price = value[5]


    query_pick_computer_by_ID = f"INSERT INTO orders(brand ,model ,computerID ,customerID ,price )values('{brand}','{model}',{selection},{custID},{price })";
    cursor.execute(query_pick_computer_by_ID)
    cnx.commit()
    logging.info("a new order was placed")
def add_new_computer():
    while True:
        try:
            brand = str(input("Enter Computer Brand :>>>\n"))
            mat = re.match("^[0-9 ]+$", brand)
            if mat != None:
                raise ValueError
        except ValueError as ve:
            print(f"Brand Name can not be an Integer : Enter a String \n")
        else:
            break

    while True:
        try:
            model= str(input("Enter computer Model:>>>\n"))
            mat = re.match("^[0-9 ]+$", model)
            if mat != None:
                raise ValueError
        except ValueError as ve:
            print("Model name can not be an Integer : Enter a String \n")
        else:
            break

    valid = False
    while valid == False:
        try:
            ram = int(input("Enter Computer RAM Size (GB):>>>\n"))
            valid=True
        except ValueError:
            print("RAM must be an Integer Value : \n")
            valid = False
        else:
            continue

    value= False
    while value == False:
        try:
            disk = int(input("Enter Computer DISK Size (GB):>>>\n"))
            value =True
        except ValueError:
            print("DISK size must be an Integer Value : \n")
            value=False
        else:
            pass

    res = False
    while res == False:
        try:
            price = int(input("Enter Computer PRICE ($):>>>\n"))
            res= True
        except ValueError:
            print("PRICE must be an Integer Value : \n")
            res =False
        else:
            pass

    comp = computer(brand,model,ram,disk,price)

    print(f"New Computer added to Invenory : \n{comp}")
    query_add_computer = f"INSERT INTO computer (brand,model,ram,disk,price)VALUES ('{comp.brand}','{comp.model}',{comp.ram},{comp.disk},{comp.price}) "

    cursor.execute(query_add_computer)
    cnx.commit()
    logging.info("new computer was added to the inventory")
def add_new_customer():
    print(f"Adding a new customer.....Enter: \tNAME \tADDRESS \tAGE\n")
    while True:
        try:
            name = str(input(f"Enter customer name:>>>"))
            if re.search("[a-zA-Z]",name):
                break
            else:
                raise ValueError
                print(f"\nInvalid Name Format")
        except ValueError as ve:
            print(f"Invalid name Format ,    NAME MUST BE A STRING:")
        else:
            break

    while True:
        try:
            address = str(input(f"Enter customer Address:>>>"))
            if re.search("[a-zA-Z0-9]",address):
                break
            else:
                raise ValueError
                print(f"\nInvalid Name Format")
        except ValueError as ve:
            print(f"Invalid name Format ,    NAME MUST BE A STRING:")
        else:
            break

    valid = False
    while not valid:
        try:
            age = int(input(f"Enter customer age: >>>"))
            valid= True
        except:
            print(f"Invalid Input ,Customer AGE must be an Integer ")

    new_customer=customer(name,address,age)

    query_add_new_customer = f"INSERT INTO customers (name,address,age)VALUES ('{new_customer.name}','{new_customer.address}',{new_customer.age}) "

    cursor.execute(query_add_new_customer)
    cnx.commit()
    print(f"New Customer Details :\n{new_customer}\n")
    logging.info("new customer was created ")

    cursor.execute(f"select * from customers where name = '{name}' and address = '{address}' and age ={age}; ")
    for record in cursor :
        print(f"Your customer ID = {record[0]} \nYour ID and name will be used to Log into the portal next time ")


"""*******VIEW RECORDS FUNCTIONS*******"""
def view_customer_orders():
    valid= False
    while not valid:
        try:
            custID = int(input("Enter Customer ID to view Their Orders: >>>\n"))
            valid = True
        except:
            print("Invalid Input . Customer ID must be an Integer ")
    query_show_customer_order = f"SELECT * FROM orders WHERE customerID ={custID}"
    cursor.execute(query_show_customer_order)
    for record in cursor:
        print(record)
        if record == None:
            print("Empty Register ")
        logging.info("all placed orders were viewed")

def view_all_Admin():
    query_all_admin = "SELECT * FROM admin"
    cursor.execute(query_all_admin)
    for record in cursor:
        print(record)
    logging.info("all admins deatils were viewed")

def view_all_computers():
    query_show_all_computer = "SELECT * FROM computer"
    cursor.execute(query_show_all_computer)
    for record in cursor:
        print(record)
    logging.info("computer inventory was viewed")

def view_all_customers():
    query_show_customer = "SELECT * FROM customers"
    cursor.execute(query_show_customer)
    for record in cursor:
        print(record)
    logging.info("all customers list was viewed")

def view_all_orders():
    query_show_customer_order = "SELECT * FROM orders"
    cursor.execute(query_show_customer_order)
    for record in cursor:
        print(record)
    logging.info("all orders placed was viewed")


"""*******MODIFY RECORDS FUNCTIONS*******"""
def modify_admin():
    cursor.execute(f"SELECT * FROM  admin")
    for record in cursor:
        print(record)

    admin_id = input("Enter the Admin ID :\n")
    query_computer_to_modify = f"SELECT * FROM admin WHERE adminID ={admin_id}"
    cursor.execute(query_computer_to_modify)
    for record in cursor:
        print(record)

    for record in cursor:
        print(f"\t{record[0]}: NAME: '{record[1]}', PASSCODE: {record[2]}")
    col_to_modify = input("Select Column to modify(name ,passcode)")
    modified_value = input(f"What will you want to change the  {col_to_modify} to? \n")

    if col_to_modify == 'name':
        new_value = f"UPDATE admin SET {col_to_modify} = '{modified_value}' WHERE adminID ={admin_id}"
    elif col_to_modify == 'passcode':
        new_value = f"UPDATE admin SET {col_to_modify} = '{modified_value}' WHERE adminID ={admin_id}"
    else:
        pass
    cursor.execute(new_value)
    cnx.commit()
    logging.info(" An Admin record was modified")

def modify_customer_records():
    query_customer_details="SELECT * FROM customers"
    cursor.execute(query_customer_details)

    for record in cursor:
        print(f"\t{record[0]}: NAME: {record[1]}, ADDRESS: {record[2]},AGE: {record[3]} ")
    customer_to_modify= input("Enter customers ID")
    col_to_modify= input("Select Column to modify(name,address,age)")
    modified_value= input(f"what will ou want to change {col_to_modify} to?")

    if col_to_modify =='name':
        new_value=f"UPDATE customers SET {col_to_modify} = '{modified_value}' WHERE customerID ={customer_to_modify}"
    elif col_to_modify== 'address':
        new_value = f"UPDATE customers SET {col_to_modify} = '{modified_value}' WHERE customerID ={customer_to_modify}"
    elif col_to_modify== 'age':
        new_value = f"UPDATE customers SET {col_to_modify} = '{modified_value}' WHERE customerID ={customer_to_modify}"
    else:
        pass
    cursor.execute(new_value)
    cnx.commit()
    logging.info("Customer details was modified  ")

def modify_computer():
    cursor.execute(f"SELECT * FROM  computer")
    for rec in cursor:
        print(rec)

    valid = False
    while valid != True:
        try:
            computer_id = input("Enter the Computer ID :\n")
            valid = True
        except:
            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

    query_computer_to_modify= f"SELECT * FROM computer WHERE computerID ={computer_id}"
    cursor.execute(query_computer_to_modify)
    for record in cursor:
        print(record)

    for record in cursor:
        print(f"\t{record[0]}: BRAND: {record[1]}, MODEL: {record[2]},RAM: {record[3]}, DISK: {record[2]},PRICE: {record[3]}  ")
    restart =True
    while restart == True:
        col_to_modify = input("Select Column to modify(brand ,model,ram,disk,price)")
        if col_to_modify not in ("brand" ,"model","ram","disk","price"):
            print("Wrong Format ")
            break

        modified_value = input(f"What will you want to change the  {col_to_modify} to? \n")

        if col_to_modify == 'brand':
            new_value = f"UPDATE computer SET {col_to_modify} = '{modified_value}' WHERE computerID ={computer_id}"
        elif col_to_modify == 'model':
            new_value = f"UPDATE computer SET {col_to_modify} = '{modified_value}' WHERE computerID ={computer_id}"
        elif col_to_modify == 'ram':
            new_value = f"UPDATE computer SET {col_to_modify} = {modified_value} WHERE computerID ={computer_id}"
        elif col_to_modify == 'disk':
            new_value = f"UPDATE computer SET {col_to_modify} = {modified_value} WHERE computerID ={computer_id}"
        elif col_to_modify == 'price':
            new_value = f"UPDATE computer SET {col_to_modify} = {modified_value} WHERE computerID ={computer_id}"
        else:
            print("Wrong Value Entered ")
            restart =True

        cursor.execute(new_value)
        cnx.commit()
        logging.info("Computer specification was modified ")
        exit()
"""*******VIEW DELETE FUNCTIONS*******"""

def delete_admin():
    valid = False
    while not valid:
        try:
            enter = (input("Enter master Admin password >>>>:\n"))

            valid = True
        except:
            print("Invalid Input. Enter an Integer ")

    cursor.execute(f"SELECT * FROM  masteradmin")
    for value in cursor:
        confirmPasword= value[3]

    while enter ==  confirmPasword:
        print("Successful log in ")
        logging.info("Master Admin account logged into Delete Admin Portal   ")
        cursor.execute(f"SELECT * FROM  admin")
        for record in cursor:
            print(record)
        valid = False
        while not valid:
            try:
                admin_id = int(input("Enter the Admin ID to DELETE >>>>:\n"))
                valid = True
            except:
                print("Invalid Input. Enter an Integer ")

        query_admin_to_delete = f"DELETE from admin where adminID = {admin_id}"
        cursor.execute(query_admin_to_delete)

        cnx.commit()
        print("Deletion completed..........")
        logging.info("an admin was deleted from the records")
        break
    else:
        print("Incorrect login \nOnly MASTER ADMIN can delete an Administrator")

def delete_customer_records():
    cursor.execute(f"SELECT * FROM  customers")
    for record in cursor:
        print(record)

    valid = False
    while not valid:
        try:
            cust_id = int(input("Enter the customer ID to DELETE >>>>:\n"))
            valid = True
        except:
            print("Invalid Input. Enter an Integer ")

    query_customer_to_delete = f"DELETE from customers WHERE customerID = {cust_id}"
    cursor.execute(query_customer_to_delete)
    cnx.commit()
    logging.info("A customer was deleted from the records")

def delete_computer():
    cursor.execute(f"SELECT * FROM  computer")
    for record in cursor:
        print(record)

    valid = False
    while not valid:
        try:
            computerID = int(input("Enter the computer ID to DELETE >>>>:\n"))
            valid = True
        except:
            print("Invalid Input. Enter an Integer ")

    query_computer_to_delete = f"DELETE from admin where adminID = {computerID}"
    cursor.execute(query_computer_to_delete)

    cnx.commit()
    logging.info("A computer was deleted from the system ")