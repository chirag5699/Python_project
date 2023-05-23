from Counsellor import *
from Student_Details import *
def Student():
   
    Serial_num=int(input("Enter Serial Number : "))
    if Serial_num in store.keys():
        print("---------------------------------------")
        print("first name -->",store[Serial_num]["First_Name"])
        print("---------------------------------------")
        print("Last_name  -->",store[Serial_num]["Last_Name"])
        print("---------------------------------------")
        print("Countect_Number ->",store[Serial_num]["Countect_Number"])
        print("---------------------------------------")
        print("Subject ->",store[Serial_num]["Subject"])
        print("---------------------------------------")
        print("Marks ->",store[Serial_num]["Marks"])
        print("---------------------------------------")
        print("Fees ->",store[Serial_num]["Fees"])
        print("---------------------------------------")

    else:
        print("Not A Student Serial Number")
        
        