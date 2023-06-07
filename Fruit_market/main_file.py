from manger import *    # import manger (*) mines  oll function import
from customer import * 
import customer # import customer (*) mines  oll function import

import datetime
while True:
    print("Wellcome To Fruit Market")
    item = '''\n      
    1) Manger               
    2) Customer
    3) Go To Exit
    '''
    print(item)   # display  role
    s_role = int(input("Enter Your Role : "))  # input role
    if s_role == 1:  # user select 1 role to manger
        print("Fruit Market manger")
        choice = '''
        1)Add Fruit Stock
        2)View Fruit Stock
        3)Update Fruit Stock   
        '''
        while True:
            print(choice)  # display choice
            s_choice = int(input("Select Your Choice : "))
            if s_choice == 1:  # user select 1 choice to Add fruit stock
                Add_Fruit_Stock()  # function call
                yn = input(
                    "Press [Y] for manger file  and [N] for main manu  : ")
                if yn == 'y':  # user 'y' for yes to continue to program
                    continue
                elif yn == 'n':  # uesr 'n' for no to break to program
                    break
            elif s_choice == 2:  # user select 2 choice to View fruit stock
                View_Fruit_Stock()  # function call
                yn = input(
                    "Press [Y] for manger file  and [N] for main manu  : ")
                if yn == 'y':  # user 'y' for yes to continue to program
                    continue
                elif yn == 'n':  # user 'n' for no to break to program
                    break
            elif s_choice == 3:
                Update_Fruit_Stock()  # function call
                yn = input(
                    "Press [Y] for manger file  and [N] for main manu  : ")
                if yn == 'y':  # user 'y' for yes to continue to program
                    continue
                elif yn == 'n':  # user 'n' for no to break to program
                    break
    elif s_role == 2:  # user select 2 role to customer
        customer_reole()  # function call

    elif s_role == 3:  # user select 3 role to Got back to program
        Customer_bill()   # fanction call
        break


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    # database=" "
)
# mycursor = mydb.cursor()
# query = """ create database fruit_market"""
# mycursor.execute(query)
# mydb.commit()

mycursor = mydb.cursor()
query = """ use fruit_market """
mycursor.execute(query)
mydb.commit()

# mycursor = mydb.cursor()
# query =f"""create table customer(
#     name varchar(20),
#     Bill_num int,
#     total_amount int
#     )"""
# mycursor.execute(query)
# mydb.commit()


