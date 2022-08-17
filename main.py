from class_files import admin,customer,computer,orders
from method_files import insert_records, admin_ops, customer_ops, view_customer_orders, modify_computer, \
    modify_customer_records, modify_admin, view_all_customers, add_new_order
import logging
import mysql.connector
import mysql_config as c

def main():
    try:
        cnx = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database="Project_1")
        cursor = cnx.cursor()
    except mysql.connector.Error as mce:
        print(mce.msg)
        return
    except Exception as e:
        print("ERROR:Exiting the program")
        return
    logging.basicConfig(filename="citizencomputerstore.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')


insert_records()

if __name__ == "__main__":
    main()