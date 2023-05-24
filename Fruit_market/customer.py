from manger import *
import datetime
def customer_reole():  # function defination
    while True : #user while loop
        print(store)
        dict1={}
        user_choice=input("select Your Fruit : ")
        if user_choice in store.keys():  #user_choice in store.keys for if statment
            F_qty=int(input("Enter Fruit Quntity : "))
            store[user_choice]["quantity"]-=F_qty  #- to user fruit Qty
            dict1={user_choice:{"quantity":F_qty,"Amount":F_qty * store[user_choice]["Price"]}}
            print(dict1)
            print("Avelable Fruits : ")
            print("---------------------------------------")

        for i in store.keys():
            print(f"fruit name is : {i}")
            print(i,"fruit quantity-->",store[i]["quantity"])
            print(i,"fruit price --> ",store[i]["Price"])
            print("---------------------------------------")
        else:
            print("Fruit not exiesting your stock")
        yn=input("Press Y for more shoping and N for Exit : ")
        if yn == 'y':
            continue
        elif yn == 'n':
            break
def Customer_bill():
    print(store)
    total_amount=0
    print("add to txt file__ ")
    file=open("dev.txt","a")
    file.write("\n\nFruit Market Customer\n")
    name=input("Enter Customer Name : ")
    file.write(f"Name : {name}\n")
    Bill_num=int(input("Enter Bill Number : "))
    file.write(f"Bill No. : {Bill_num}\n")
    file.write("------------------------------------\n")
    file.write(f"Bill No. : {Bill_num}\n")
    x=datetime.datetime.now()
    print(file.write(x.strftime("%Y/%B/%d, %H:%M:%S\n")))
    file.write("------------------------------------\n")
    file.write("item\t\tQty\t\tprice\n")
    file.write("------------------------------------\n")
    for i in store:
            qty=store[i]["quantity"]
            pr=store[i]["Price"]
            file.write(f"{i}\t\t{qty}\t\t{pr}\n")
            total_amount+=pr
    file.write("------------------------------------\n")
    file.write(f"Total Amount\t\t{total_amount}\n")
    file.write("------------------------------------\n") 
    
    
    print(f"Bill No. : {Bill_num}\n")
    print("------------------------------------\n")
    print(f"Bill No. : {Bill_num}\n")
    x=datetime.datetime.now()
    print(x.strftime("%Y/%B/%d, %H:%M:%S\n"))
    print("------------------------------------\n")
    print("item\t\tQty\t\tprice\n")
    print("------------------------------------\n")
    for i in store:
            qty=store[i]["quantity"]
            pr=store[i]["Price"]
            print(f"{i}\t\t{qty}\t\t{pr}\n")
            total_amount+=pr
    print("------------------------------------\n")
    print(f"Total Amount\t\t{total_amount}\n")
    print("------------------------------------\n")                    
