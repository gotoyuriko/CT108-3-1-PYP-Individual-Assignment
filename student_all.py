import file_handle as f


def view_details():
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\t*** View Detail of ***\n\ta. Sport\n\tb. Sport Schedule\n\tc. Exit")

        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            view_details_a()
        elif choice == "b":
            view_details_b()
        elif choice == "c":
            break
        else:
            print("\n\tPlease Enter a ~ c")

        continuey = input("\n\tEnter 'y' to continue or any key to back: ")


def view_details_a():  # View Datail of Sport
    print("\n*** View Detail of Sport ***\n\n\t")

    sport_list = f.sport_read()

    for sport in sport_list:
        print("\tSport: "+str(sport["Sport Name"]))
        print("\t"+str(sport["Description"]))
        print()


def view_details_b():  # View Datail of Sport Schedule
    print("\n*** View Detail of Sport Schedule ***\n\n\t")

    sport_list = f.sport_read()
    schedule_list = f.schedule_read()

    for schedule in schedule_list:
        for sport in sport_list:
            if schedule["Sport Code"] == sport["Sport Code"]:
                print("\tSport: "+str(sport["Sport Name"]))
        print("\tDate: "+schedule["Date"])
        print("\tStart Time: "+schedule["Start Time"])
        print("\tEnd Time: "+schedule["End Time"])
        print()


def student_signup():
    student = {}
    print("\n*** Student Sign Up ***")

    student["Student ID"] = input("\n\tEnter your email: ")
    student["Password"] = input("\tEnter your password: ")
    student["Name"] = input("\tEnter your name: ")

    # select a coach who teaches students his/her sport
    coach_name = select_coach(student)

    print("\n\t★★★ Complete ★★★\n")
    print("\tYour Email: " + student["Student ID"])
    print("\tYour Name: "+student["Name"])
    print("\tCoach Name: " + coach_name)

    student_list = f.student_read()
    student_list.append(student)
    f.student_write(student_list)
    return


def select_coach(student):
    coach_list = f.coach_read()

    print("\n\tSelect Coach")
    for coach in coach_list:
        print("\t"+str(coach_list.index(coach)+1) + ": ",
              str(coach["Name"]), "("+str(coach["Sport Name"])+")")

    while 1:
        num = input("\n\tChoose a number: ")
        try:
            num = int(num)
            for coach in coach_list:
                if num == (coach_list.index(coach)+1):
                    student["Coach ID"] = coach["Coach ID"]
                    coach_name = coach["Name"]
                    return coach_name
            print("\n\tThe number is out of range")
            continue
        except:
            print("\n\tPlease enter the number")
            continue
