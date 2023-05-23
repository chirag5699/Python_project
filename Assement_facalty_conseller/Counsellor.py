store={}
def Add_Student():
    A_number=int(input("Enter student Serial Number : "))
    A_Fname=input("Enter student First Name : ")
    A_Lname=input("Enter student Last Name : ")
    A_Cnumber=int(input("Enter student Contect Number : "))
    subjectlist=[]
    marklist=[]
    feeslist=[]
    for i in range(1,3):
        A_subject=input(f"Enter student Subject {i}: ")
        subjectlist.append(A_subject)
        A_mark=int(input(f"Enter student marks {i}: "))
        marklist.append(A_mark)
        A_fees=int(input(f"Enter student Fees {i}: "))
        feeslist.append(A_fees)
        print("--------------------------------------")
    

    global store     # store student details
    store.update({A_number:{"First_Name":A_Fname,"Last_Name":A_Lname,"Countect_Number":A_Cnumber,
                                         "Subject":subjectlist,"Marks":marklist,"Fees":feeslist}})


def Remove_Student():
    print(" choice Remove Student ")
    serial_number=int(input("Enter  student Remove Serial Number : "))
    if serial_number in store.keys():
        store.pop(serial_number)  # remove serial number
    else:
        print("Student not exiesting your Student List.")

def view_all_student():
    print(" chioce View All Student")
    for Serial_num in store:
        print(f"serial num = {Serial_num}\n")
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
def Specific_Student():
    print("Enter serial number to show student details ")
    Serial_num=int(input("Enter Serial Number : "))
    if Serial_num in store:
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