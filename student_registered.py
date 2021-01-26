import file_handle as f
import student_all as st_a


def student_login():
    continuey = "y"
    while continuey == "y":
        print("\n*** Student Log In ***\n\n\tEnter your email and password")

        student_username = input("\tEmail： ")
        student_password = input("\tPassword： ")

        # validate username and password
        student_list = f.student_read()
        for student in student_list:
            if student_username == student["Student ID"] and student_password == student["Password"]:
                student_id = student["Student ID"]
                return True, student_id  # login sccessgul and return your student ID
        print("\n\tIncorrect username or password\n")

        continuey = input(
            "\n\tEnter 'y' to type username and password again: ")


def view_details(student_id):
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\t*** View Datail of ***\n\ta. Coach\n\tb. Self-Record\n\tc. Registered Sport Schedule\n\td. Exit")

        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            view_details_a()
        elif choice == "b":
            view_details_b(student_id)
        elif choice == "c":
            view_details_c(student_id)
        elif choice == "d":
            return
        else:
            print("\n\tPlease Enter a ~ d")

        continuey = input("\n\tEnter 'y' to continue or any key to back: ")


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


def view_details_c(student_id):
    coach_id = ""
    coach_name = ""
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            coach_id = student["Coach ID"]

    coach_list = f.coach_read()
    for coach in coach_list:
        if coach["Coach ID"] == coach_id:
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
            coach_name = ""
            while continue_modify == "m":
                print("\n*** Modify Records of Self-Record ***\n\n\tWhich record do you want to modify?\n\t1. Your Email\n\t2. Password\n\t3. Your Name\n\t4. Select Coach\n\t5. Exit")
                num = input("\n\tEnter your choice: ")
                try:
                    num = int(num)
                    if num == 1:
                        student["Student ID"] = input(
                            "\n\tPlease Enter your email: ")
                    elif num == 2:
                        old_passowrd = input(
                            "\n\tPlease Enter the current Password: ")
                        if old_passowrd == student["Password"]:
                            student["Password"] = input(
                                "\n\tPlease Enter the new Password: ")
                        else:
                            print("\n\tIncorrect Password")
                            continue
                    elif num == 3:
                        student["Name"] = input("\n\tPlease Enter your name: ")
                    elif num == 4:
                        coach_name = st_a.select_coach(student)
                    elif num == 5:
                        break
                    else:
                        print("The number is out of range")
                        continue
                except:
                    print("\n\tWrong Input")
                    continue

                continue_modify = input(
                    "\n\tEnter \'m\' (continue to modify), or any key(back): ")

            # udpate student records into student file
            f.student_write(student_list)

            # print student info
            print("\n\t★★★Complete★★★\n")
            print("\tYour Email: "+student["Student ID"])
            print("\tYour Name: "+student["Name"])
            print("\tCoach Name: " + coach_name)

            # update your student ID
            student_id = student["Student ID"]
            return student_id


def feedback_star(student_id):
    coach_id = ""
    coach_name = ""

    # read coach id whose chach teaches the student.
    student_list = f.student_read()
    for student in student_list:
        if student["Student ID"] == student_id:
            coach_id = student["Coach ID"]

    # read coach name
    coach_list = f.coach_read()
    for coach in coach_list:
        if coach["Coach ID"] == coach_id:
            coach_name = coach["Name"]

    print("\n*** Please give us your feedback on your coach【"+coach_name+"】***\n")
    print("\t1: \"very poor performance\"\n\t5: \"excellent performance\"")

    count = 0
    actial_rating = 0
    rating_ave = 0
    rating_int = 0
    feedback = {}

    rating_list = f.rating_read()
    for rating in rating_list:
        if rating["Coach ID"] == coach_id:
            # get feedback
            feedback["Coach ID"] = rating["Coach ID"]
            feedback["Description"] = input(
                "\n\tPlease give him/her feedbacks: ")

            # read count and actual rating(float)
            count = rating["Count"]
            actial_rating = float(rating["Actual Rating"])

            while 1:
                new_rating = input("\tEnter from 1 to 5: ")
                try:
                    new_rating = int(new_rating)
                    if new_rating > 0 and new_rating <= 5:
                        # calculate average rating
                        total_num = actial_rating * count
                        total_num += new_rating
                        count += 1
                        rating_ave = total_num / count

                        # Round float to integer
                        if rating_ave >= 1 and rating_ave < 1.5:
                            rating_int = 1
                        elif rating_ave >= 1.5 and rating_ave < 2.5:
                            rating_int = 2
                        elif rating_ave >= 2.5 and rating_ave < 3.5:
                            rating_int = 3
                        elif rating_ave >= 3.5 and rating_ave < 4.5:
                            rating_int = 4
                        elif rating_ave >= 4.5 and rating_ave <= 5.0:
                            rating_int = 5

                        rating["Rating"] = rating_int

                        print("\t★★★ Thank you !! ★★★\n")
                        break
                    else:
                        print("\n\tThe number is out of range!!")
                        continue

                except:
                    print("\n\tWrong input")
                    continue

            # Update count and actual rating(the first desimal point)
            rating["Count"] = count
            rating["Actual Rating"] = "{:.1f}".format(rating_ave)
            f.rating_write(rating_list)

    # add feedback into feedback textfile
    feedback_list = f.feedback_read()
    feedback_list.append(feedback)
    f.feedback_write(feedback_list)

    # Update rating in the coach.txt file
    for coach in coach_list:
        if coach["Coach ID"] == coach_id:
            coach["Rating"] = rating_int
            f.coach_write(coach_list)
