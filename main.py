import admin as ad
import student_all as st_a
import student_registered as st_r


print("\n*** Welcome to REAL CHAMPION APORT ACADEMY! ***\n\n\tWho are you?\n\t1. Admin\n\t2. All Students (Registered / Not-Registered)\n\t3. Registered Student")

user = input("\n\tEnter the number: ")
try:
    user = int(user)
    if user == 1:
        if ad.admin_login():  # 1. Admin
            while 1:
                print("\n*** Admin Menu ***\n\n\t1. Add Record\n\t2. Display All Records\n\t3. Search Specific Record\n\t4. Sort and Display Record\n\t5. Modify Record\n\t6. Exit")
                choice = input("\n\tEnter your choice: ")
                try:
                    choice = int(choice)
                    if choice == 1:
                        ad.admin_add()
                    elif choice == 2:
                        ad.admin_display()
                    elif choice == 3:
                        ad.admin_search()
                    elif choice == 4:
                        ad.admin_sort()
                    elif choice == 5:
                        ad.admin_modify()
                    elif choice == 6:
                        print("\n*** Log Out ***")
                        break
                    else:
                        print("\n\tPlease enter 1 ~ 6")
                        continue
                except:
                    print("\n\t", str(choice), "is not a number")
                    continue

    elif user == 2:  # 2. All Students (Registered / Not-Registered)
        while 1:
            print("\n*** Student Menu ***\n\n\t1. View details of...\n\t2. If new student Register to Access other  Details\n\t3. Exit")
            choice = input("\n\tEnter your choice: ")
            try:
                choice = int(choice)
                if choice == 1:
                    st_a.view_details()
                elif choice == 2:
                    st_a.student_signup()
                elif choice == 3:
                    print("\n\tLog Out")
                    break
                else:
                    print("\n\tPlease enter 1 ~ 3")
                    continue
            except:
                print("\n\t" + str(choice), "is not a number")
                continue

    elif user == 3:  # 3. Registered Student
        success, student_id = st_r.student_login()
        if success:
            while 1:
                print("\n*** Resistered Student Menu ***\n\n\t1. View Detail of\n\t2. Modify Self Record\n\t3. Provide feedback and Star to Coach\n\t4. Exit")
                choice = input("\n\tEnter your choice: ")
                try:
                    choice = int(choice)
                    if choice == 1:
                        st_r.view_details(student_id)
                    elif choice == 2:
                        student_id = st_r.modify_selfrecord(student_id)
                    elif choice == 3:
                        st_r.feedback_star(student_id)
                    elif choice == 4:
                        print("\n*** Log Out ***")
                        break
                    else:
                        print("\n\tPlease enter 1 ~ 6")
                        continue
                except:
                    print("\n\t"+str(choice), "is not a number")
                    continue

    else:
        print("\n\tPlease enter 1 ~ 3")
except:
    print("\n\t"+str(user), "is not a number")

print("\n★★★ See You ★★★")
