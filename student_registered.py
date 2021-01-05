import file_handle as f
import student_all as st_a


def student_login():
    continuey = "y"
    while continuey == "y":
        print("\n*** Student Log In ***\n\n\tEnter your email and password")
        student_username = input("\tEmail：")
        student_password = input("\tPassword：")
        student_list = f.student_read()
        for student in student_list:
            if student_username == student["Student ID"] and student_password == student["Password"]:
                student_id = student["Student ID"]
                return True, student_id  # login sccessgul with your student ID
        print("\n\tIncorrect username or password\n")
        continuey = input(
            "\n\tEnter 'y' to type username and password again: ")


def view_details(student_id):
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\t*** View Datail of ***\n\ta. Coach\n\tb. Self-Record\n\tc. Registered Sport Schedule")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            view_details_a()
        elif choice == "b":
            view_details_b(student_id)
        elif choice == "c":
            view_details_c(student_id)
        else:
            print("\n\tPlease Enter a or b")
        continuey = input("\n\tEnter 'y' to continue: ")
        if continuey != "y":
            break


def view_details_a():
    print("\n*** View Detail of Coach ***\n")
    coach_list = f.coach_read()
    for coach in coach_list:
        print("\tCoach: "+str(coach["Name"]))
        print("\tSport Center: "+str(coach["Sport Center Name"]))
        print("\tSport: "+str(coach["Sport Name"]))
        print("\tSport Fees: "+str(coach["Horly Rate (RM/h)"]) + "(RM/h)")
        print("\tOverall performance (Rating): "+str(coach["Rating"]))
        print()


def view_details_b(student_id):
    print("\n*** View Detail of Self-Record ***\n")
    read_selfrecord(student_id)


def view_details_c(student_id):
    coach_id = ""
    coach_name = ""
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            coach_id = student["Coach ID"]

    coach_list = f.coach_read()
    for coach in coach_list:
        coach_name = coach["Name"]

    schedule_list = f.schedule_read()
    print("\n\t*** The schedule of your Coach 【"+coach_name+" 】is Below ***\n")
    for schedule in schedule_list:
        if schedule["Coach ID"] == coach_id:
            print("\tDate: "+str(schedule["Date"]))
            print("\tStart Time: "+str(schedule["Start Time"]))
            print("\tEnd Time: "+str(schedule["End Time"]))
            print()


def modify_selfrecord(student_id):
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            continue_modify = "m"
            while continue_modify == "m":
                print("\n*** Modify Records of Self-Record ***\n\n\tWhich record do you want to modify?\n\t1. Your Email\n\t2. Password\n\t3. Your Name\n\t4. Select Coach")
                num = input("\n\tEnter your choice: ")
                modify_coach(num, student)
                continue_modify = input(
                    "\n\tEnter \'m\' to continue to modify: ")

            f.student_write(student_list)
            print("\n\t★★★Complete★★★\n")
            print("\tYour Email: "+student["Student ID"])
            print("\tPassword: "+student["Password"])
            print("\tYour Name: "+student["Name"])
            coach_list = f.coach_read()
            for coach in coach_list:
                if coach["Coach ID"] == student["Coach ID"]:
                    print("\tCoach Name: "+coach["Name"])
                    print("\tSport Center: " +
                          coach["Sport Center Name"])
                    print("\tSport: "+coach["Sport Name"])
                    print("\tSport Fees: " +
                          str(coach["Horly Rate (RM/h)"])+"(RM/h)")


def feedback_star(student_id):
    coach_id = ""
    coach_name = ""
    coach_list = f.coach_read()
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            coach_id = student["Coach ID"]
    for coach in coach_list:
        if coach["Coach ID"] == coach_id:
            coach_name = coach["Name"]

    print("\n*** Please give us your feedback on your coach【"+coach_name+"】***\n")
    print("\t1: \"very poor performance\"\n\t5: \"excellent performance\"")

    count = 0
    old_rating = 0
    rating_ave = 0
    rating_list = f.rating_read()

    for rating in rating_list:
        if rating["Coach ID"] == coach_id:
            count = rating["Count"]
            old_rating = float(rating["Actual Rating"])
            rating_ave, count, actial_rating = rating_calculation(
                count, old_rating)
            rating["Count"] = count
            rating["Rating"] = rating_ave
            rating["Actual Rating"] = "{:.1f}".format(actial_rating)
            f.rating_write(rating_list)

    for coach in coach_list:
        if coach["Coach ID"] == coach_id:
            coach["Rating"] = rating_ave
            f.coach_write(coach_list)


def modify_coach(num, student):
    try:
        num = int(num)
        if num == 1:
            student["Student ID"] = input("\n\tPlease Enter your email: ")
        elif num == 2:
            old_passowrd = input("\n\tPlease Enter the current Password: ")
            if old_passowrd == student["Password"]:
                student["Password"] = input(
                    "\n\tPlease Enter the new Password: ")
                return
            else:
                print("\n\tIncorrect Password")
                return
        elif num == 3:
            student["Name"] = input("\n\tPlease Enter your name: ")
        elif num == 4:
            st_a.select_coach(student)
        else:
            print("The number is out of range")
    except:
        print("\n\tWrong Input")


def read_selfrecord(student_id):
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            print("\tYour Email: "+student["Student ID"])
            print("\tYour Name: "+student["Name"])
            coach_list = f.coach_read()
            for coach in coach_list:
                if coach["Coach ID"] == student["Coach ID"]:
                    print("\tCoach Name: "+coach["Name"])
                    print("\tSport Center: " + coach["Sport Center Name"])
                    print("\tSport: "+coach["Sport Name"])
                    print("\tSport Fees: " +
                          str(coach["Horly Rate (RM/h)"])+"(RM/h)")


def rating_calculation(count, old_rating):
    while 1:
        new_rating = input("\tEnter from 1 to 5: ")
        try:
            new_rating = int(new_rating)
            if new_rating > 0 and new_rating <= 5:
                total_num = old_rating * count
                total_num += new_rating
                count += 1
                actial_rating = total_num / count
                rating_int = rating_comparison(actial_rating)
                print("\n\tYour rating:", new_rating)
                print("\t★★★ Thank you !! ★★★\n")
                return rating_int, count, actial_rating
            else:
                print("\n\tThe number is out of range!!")

        except:
            print("\n\tWrong input")
            continue


def rating_comparison(r):
    if r >= 1 and r < 1.6:
        r = 1
    elif r >= 1.6 and r < 2.6:
        r = 2
    elif r >= 2.6 and r < 3.6:
        r = 3
    elif r >= 3.6 and r < 4.6:
        r = 4
    elif r >= 4.6 and r <= 5.0:
        r = 5
    return r
