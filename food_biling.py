import datetime
print("--------- wellcome to my hotel -------- ")
items='''no.         item            price
        1.          Dal.fry         180:00
        2.          dhoosa          180.50
        3.          veg.dish        350:00
        4.          suup            80:00
        5.  Exit Go to bill'''
data={}
while True:
    print(items)
    net_amount=0

    S_items=int(input("Enter item 1,2,3,4,5 :"))    
    if S_items==1:
        print("thank you for order \n you have select  Dal.fry")
        qun1=int(input("Enter Quntity :"))
        amount1 = qun1 * 180
        print("------------------------")
        print(f"Amount is {amount1}")
        print("------------------------")
        net_amount1=+amount1
        if "items1" in data.keys():
            data["items1"]["quantity"]+=qun1
            data["items1"]["amount"]+=amount1
        else:
            data.update({"items1":{"quantity":qun1,"amount":amount1}})
        
    elif S_items==2:
        print("thank you for order \n you have select  dhoosa")
        qun2=int(input("Enter Quntity :"))
        amount2 =qun2 * 180.50
        print("------------------------")
        print(f"Amount is {amount2}")
        print("------------------------")
        net_amount2=+amount2
        if "items2" in data.keys():
            data["items2"]["quantity"]+=qun2
            data["items2"]["amount"]+=amount2
        else:
            data.update({"items2":{"quantity":qun2,"amount":amount2}})
       
    elif S_items==3:
        print("thank you for order \n you have select  veg.dish")
        qun3=int(input("Enter Quntity :"))
        amount3 =qun3 * 350.00
        print("------------------------")
        print(f"Amount is {amount3}")
        print("------------------------")
        net_amount3=+amount3
        if "items3" in data.keys():
            data["items3"]["quantity"]+=qun3
            data["items3"]["amount"]+=amount3
        else:
            data.update({"items3":{"quantity":qun3,"amount":amount3}})
        
        
    elif S_items==4:
        print("thank you for order \n you have select  shoup")
        qun4=int(input("Enter Quntity :"))
        amount4 =qun4 * 80.00
        print("------------------------")
        print(f"Amount is {amount4}")
        print("------------------------")
        net_amount4=+amount4
        if "items4" in data.keys():
            data["items4"]["quantity"]+=qun4
            data["items4"]["amount"]+=amount4
        else:
            data.update({"items4":{"quantity":qun4,"amount":amount4}})
        
    elif S_items==5:
        print("Thank you for visit")
        break
print(data)
keys_all=data.keys()
final_amount=0
for i in keys_all:
    main_data=data[i]
    final_amount+=main_data["amount"]
file=open("Bill.txt","a")    
print(file.write("== Your bill ==\n"))
print(file.write("--------------------------------------------------------\n"))
x=datetime.datetime.now()
print(file.write(x.strftime("%Y/%B/%d, %H:%M:%S\n")))
print(file.write("item\t\t\tqun\t\t\tamount\n"))

print(file.write("--------------------------------------------------------\n"))

for i in keys_all:
    main_data=data[i]
    q=data[i]["quantity"]
    a=data[i]["amount"]
    print(file.write(f"{i}\t\t\t{q}\t\t\t{a}\n"))
print(file.write("--------------------------------------------------------"))
print(file.write("--------------------------------------------------------\n"))
print(file.write(f"Total  amount {final_amount}\n"))
print(file.write("---🙏🙏🙏Thank you for visit again🙏🙏🙏---\n"))
file.close()