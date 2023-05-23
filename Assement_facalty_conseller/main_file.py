from Counsellor import *
from Faculty import *
from Student_Details import *
while True:
    item='''
    1) Press 1 For Counsellor
    2) press 2 For Faculty
    3) Press 3 For Student
    4) Press 4 For Go To Exit
    '''
    print(item)
    role=int(input("Enter Role ID : "))
    if role == 1:  # For Counsellor 
        print("Enter 1 Choice by Counsellor")
        Counsellor_data='''
        1.Add Student
        2.Remove Student
        3.View All Student
        4.view Specific Student 
        '''
        while True:
            print(Counsellor_data)
            user_choice=int(input("Choice by Counsellor : "))
            if user_choice == 1:
                print("select add student \n  Enter student details")
                Add_Student()  # fanction call by counseller file
                ans=input("Press [Y] for yes and [N] for no : ")
                if ans == 'y':  #user 'y' for yes to continue to program
                    continue
                elif ans == 'n':  #uesr 'n' for no to break to program
                    break
            elif user_choice == 2:
                Remove_Student()  # fanction call by counseller file
                ans=input("Press [Y] for yes and [N] for no : ")
                if ans == 'y':  #user 'y' for yes to continue to program
                    continue
                elif ans == 'n':  #uesr 'n' for no to break to program
                    break
            elif user_choice == 3:
                view_all_student()  # fanction call by counseller file
                ans=input("Press [Y] for yes and [N] for no : ")
                if ans == 'y':  #user 'y' for yes to continue to program
                    continue
                elif ans == 'n':  #uesr 'n' for no to break to program
                    break
            elif user_choice == 4:
                Specific_Student()  # fanction call by counseller file
                ans=input("Press [Y] for yes and [N] for no : ")
                if ans == 'y':  #user 'y' for yes to continue to program
                    continue
                elif ans == 'n':  #uesr 'n' for no to break to program
                    break
    elif role == 2:  # For Faculty
        print("Enter 2 Choice by Faculty : ")
        Faculty_data='''
        1.Add Mark To Student..
        2.View All student..
        3.go for exit............
        '''
        while True:
            print(Faculty_data)
            F_Choice=int(input("Enter A Choice by Faculty : "))
            if F_Choice == 1:
                Add_mark_student()     # this fanction use to add student marks
                ans=input("Press [Y] for yes and [N] for no : ")
                if ans == 'y':
                    continue
                elif ans == 'n':
                    break
            elif F_Choice == 2:
                view_all_student()    # faction call view all student
                ans=input("Press [Y] for yes and [N] for no : ")
                if ans == 'y':
                    continue
                elif ans == 'n':
                    break
            elif F_Choice == 3:
                break    
                
    elif role == 3:  # For Student
        print("Enter 3 Choice by Student : ")
        Student()  # call fanction
    elif role == 4: # program is Terminator
        print("Thank You For Visit.")
        break