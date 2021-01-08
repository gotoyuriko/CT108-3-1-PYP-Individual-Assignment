import file_handle as f
import datetime as d


def admin_login():  # Login to Access System.
    continuey = "y"
    while continuey == "y":
        print("\n*** Admin Log In ***\n\n\tEnter username and password")

        admin_username = input("\tUser Name：")
        admin_password = input("\tPassword：")

        admin_dict = f.admin_login_read()

        if admin_username in admin_dict and admin_dict[admin_username] == admin_password:
            return True
        else:
            print("\n\tIncorrect username or password")

        continuey = input(
            "\n\tEnter 'y' to type username and password again or any key to quite: ")


def admin_add():  # Add Record
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\tAdd Records of\n\ta. Coach\n\tb. Sport\n\tc. Sport Schedule")

        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_add_a()
        elif choice == "b":
            admin_add_b()
        elif choice == "c":
            admin_add_c()
        else:
            print("\n\tPlease Enter a ~ c")

        continuey = input("\n\tEnter 'y' to continue or any key to back: ")
        if continuey != "y":
            break


def admin_add_a():  # Add Record of Coach
    coach = {}
    print("\n*** Add Records of Coach ***\n\n\tPlease Fill in your information below")
    coach["Coach ID"] = input("\n\tCoach ID: ")
    coach["Name"] = input("\tName: ")

    # Add Date
    check_date(coach)

    # check whether Horly Rate (RM/h) is number or not
    while 1:
        try:
            coach["Horly Rate (RM/h)"] = int(input("\tHorly Rate (RM/h): "))
            break
        except:
            print("\n\tPlease Enter the number")

    coach["Phone"] = input("\tPhone: ")
    coach["Adress"] = input("\tAdress: ")

    # Check whether the input of Sport center code exits or not
    while 1:
        sport_center_code = input("\tSport Center Code: ")
        sport_center_list = f.sport_center_read()
        for sport_center in sport_center_list:
            if sport_center == sport_center_code:
                coach["Sport Center Code"] = sport_center_code
                coach["Sport Center Name"] = sport_center["Sport Center Name"]
        print("\n\tThere is no", sport_center_code, "in this system")

    # Check whether the input of sport code exits or not
    while 1:
        sport_code = input("\tSport Code: ")
        sport_list = f.sport_read()
        for sport_center in sport_list:
            if sport_center == sport_code:
                coach["Sport Code"] = sport_code
                coach["Sport Name"] = sport_center["Sport Name"]
        print("\n\tThere is no", sport_code, "in this system")

    coach["Rating"] = 0

    # add records
    coach_list = f.coach_read()
    coach_list.append(coach)
    f.coach_write(coach_list)

    # print records
    print("\n\t★★★ Complete ★★★\n")
    print_records(coach)


def admin_add_b():  # Add Record of Sport
    sport = {}
    sport_list = f.sport_read()
    while 1:
        print("\n*** Add Records of Sport ***\n\n\tPlease Fill in your information below")
        sport_code = input("\tSport Code: ")
        sport_name = input("\tSport Name: ")

        # Check if the sport.txt already had input or not
        for sport in sport_list:
            if sport["Sport Code"] == sport_code or sport["Sport Name"] == sport_name:
                print("\n\t"+sport_code, "or",
                      sport_name, " are already stored")
                continue

        sport["Sport Code"] = sport_code
        sport["Sport Name"] = sport_name
        sport["Description"] = input("\tDescribe the sport: ")
        break

    sport_list.append(sport)
    f.sport_write(sport_list)

    print("\n\t★★★ Complete ★★★\n")
    print_records(sport)


def admin_add_c():  # Add Record of schedule
    schedule = {}
    schedule_list = f.schedule_read()
    while 1:
        print(
            "\n*** Add Records of Schedule ***\n\n\tPlease Fill in your information below")

        coach_id = input("\tCoach ID: ")
        coach_list = f.coach_read()
        for coach in coach_list:
            if coach["Coach ID"] == coach_id:
                # get input of schedule
                date, start_time, end_time = date_time(coach)

                schedule["Coach ID"] = coach["Coach ID"]
                schedule["Sport Code"] = coach["Sport Code"]
                schedule["Date"] = date
                schedule["Start Time"] = start_time
                schedule["End Time"] = end_time

                # add schedule into schedule.txt
                schedule_list.append(schedule)
                f.schedule_write(schedule_list)
                print("\n\t★★★ Complete ★★★\n")
                print_records(schedule)
                return
        print("\n\tWe cannot find "+coach_id+", please try again")
        continue


def admin_display():  # Display All Records
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\ta. Coach\n\tb. Sport\n\tc. Registered Students")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_display_a()
        elif choice == "b":
            admin_display_b()
        elif choice == "c":
            admin_display_c()
        else:
            print("\n\tPlease Enter a ~ c")
        continuey = input("\n\tEnter 'y' to continue or any key to back: ")
        if continuey != "y":
            break


def admin_display_a():  # Display All Records Coachs
    coach_list = f.coach_read()

    print("\n*** Here are all records of coache ***\n")
    for coach in coach_list:
        print_records(coach)


def admin_display_b():  # Display All Records Sports
    sport_list = f.sport_read()

    print("\n*** Here are all records of sport ***\n")
    for sport in sport_list:
        print_records(sport)


def admin_display_c():  # Display All Records  of Registered Students
    student_list = f.student_read()

    print("\n*** Here are all records of student ***\n")
    for student in student_list:
        print_records(student)


def admin_search():  # Search Specific Records of
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\ta. Coach by Coach ID\n\tb. Coach by overall performance (Rating)\n\tc. Sport by Sport ID\n\td. Student by Student ID")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_search_a()
        elif choice == "b":
            admin_search_b()
        elif choice == "c":
            admin_search_c()
        elif choice == "d":
            admin_search_d()
        else:
            print("\n\tPlease Enter a ~ d")
        continuey = input("\n\tEnter 'y' to continue or any key to back: ")
        if continuey != "y":
            break


def admin_search_a():  # Search Specific Records of Coach by Coach ID
    print("\n*** Search Specific Records of Coach by Coach ID ***")
    coach_list = f.coach_read()
    dict_key = "Coach ID"
    while 1:
        coach_id = input("\n\tEnter Coach ID: ")
        if search_print(coach_list, coach_id, dict_key):
            break


def admin_search_b():  # Search Specific Records of Coach by overall performance (Rating)
    print("\n*** Search Specific Records of Coach by overall performance (Rating) ***")
    coach_list = f.coach_read()
    dict_key = "Rating"
    while 1:
        try:
            rating = int(input("\n\tEnter overall performance (Rating): "))
            if search_print(coach_list, rating, dict_key):
                break
        except:
            print("\n\tPlease Enter the Number.")
            continue


def admin_search_c():  # Search Specific Records of Sport by Sport ID
    print("\n*** Search Specific Records of Sport by Sport ID ***")
    sport_list = f.sport_read()
    dict_key = "Sport Code"
    while 1:
        sport_id = input("\n\tEnter Sport ID: ")
        if search_print(sport_list, sport_id, dict_key):
            break


def admin_search_d():  # Search Specific Records of Student by Student ID
    print("\n*** Search Specific Records of Student by Student ID ***")
    student_list = f.student_read()
    dict_key = "Student ID"
    while 1:
        student_id = input("\n\tStudent ID: ")
        if search_print(student_list, student_id, dict_key):
            break


def admin_sort():  # Sort and Display Record
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\ta. Coaches in ascending order by names.\n\tb. Coaches Hourly Pay Rate in ascending order\n\tc. Coaches Overall Performance in ascending order")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_sort_a()
        elif choice == "b":
            admin_sort_b()
        elif choice == "c":
            admin_sort_c()
        else:
            print("\n\tPlease Enter a ~ c")
        continuey = input("\n\tEnter 'y' to continue or any key to back: ")
        if continuey != "y":
            break


def admin_sort_a():  # Sort Coaches in ascending order by names.
    key_name = "Name"
    sort_print(key_name)


def admin_sort_b():  # Sort Coaches Hourly Pay Rate in ascending order
    key_name = "Horly Rate (RM/h)"
    sort_print(key_name)


def admin_sort_c():  # Coaches Overall Performance in ascending order
    key_name = "Rating"
    sort_print(key_name)


def admin_modify():  # Modify Record
    continuey = "y"
    while continuey == "y":
        print("====================================================\n\n\ta. Coach\n\tb. Sport\n\tc. Sport Schedule")
        choice = input("\n\tEnter your choice: ")
        if choice == "a":
            admin_modify_a()
        elif choice == "b":
            admin_modify_b()
        # Sport Schedule
        elif choice == "c":
            admin_modify_c()
        else:
            print("\nPlease Enter a ~ c")
        continuey = input("\n\tEnter 'y' to continue or any key to back: ")
        if continuey != "y":
            break


def admin_modify_a():  # modify coach
    print("\n*** Modify Records of Coach ***")
    coach_list = f.coach_read()

    while 1:
        coach_id = input("\n\tEnter Coach ID to modify: ")
        # check coach id
        for coach in coach_list:
            if coach_id == coach["Coach ID"]:
                continue_modify = "m"
                while continue_modify == "m":
                    print("\n*** Which record do you want to modify?***\n\n\t1. Name\n\t2. Date Joined\n\t3. Date Terminated\n\t4. Horly Rate (RM/h)\n\t5. Phone\n\t6. Adress\n\t7. Sport Center\n\t8. Sport")
                    num = input("\n\tEnter your choice: ")
                    if modify_coach(num, coach):
                        continue
                    continue_modify = input(
                        "\n\tEnter \'m\' : continue to modify, or any key: back ")

                    if continue_modify != "m":
                        f.coach_write(coach_list)
                        print("\n\t★★★Complete★★★")
                        print_records(coach)
                        return

        print("\n\tThere is no " + coach_id + " in this sysmtem")


def admin_modify_b():  # Modify Sport
    print("\n*** Modify Record of Sport ***")
    while 1:
        sport_id = input("\n\tEnter Sport ID to modify: ")
        sport_list = f.sport_read()
        for sport in sport_list:
            # check coach id
            if sport_id == sport["Sport Code"]:
                sport["Sport Name"] = input("\n\tPlease Enter Sport Name: ")
                f.sport_write(sport_list)
                print("\n\t★★★Complete★★★")
                print_records(sport)
                return

        print("\n\tThere is no " + sport_id + " in this sysmtem")


def admin_modify_c():  # Modify Schedule
    print("\n*** Modify Record of Schedule ***")
    while 1:
        coach_id = input("\n\tEnter Coach ID to modify: ")
        schedule_list = f.schedule_read()

        for schedule in schedule_list:
            # check coach id
            if coach_id == schedule["Coach ID"]:
                coach_list = f.coach_read()
                for coach in coach_list:
                    if coach["Coach ID"] == coach_id:
                        date, start_time, end_time = date_time(coach)
                        schedule["Date"] = date
                        schedule["Start Time"] = start_time
                        schedule["End Time"] = end_time
                        break
                f.schedule_write(schedule_list)
                print("\n\t★★★Complete★★★")
                print_records(schedule)
                return

        print("\n\tThere is no " + coach_id + " in this sysmtem")
        continue


def print_records(dict_items):  # display records
    for dict_key in dict_items:
        print("\t"+str(dict_key)+": "+str(dict_items[dict_key]))
    print()


def search_print(list, search_key, dict_key):  # serch key
    for dict in list:
        if search_key == dict[dict_key]:
            print("\n\t*** Here are the results ***\n")
            print_records(dict)
            return True
    print("\n\tWe couldn't find " + str(search_key) + ", please try again.")
    return False


def sort_print(key_name):  # sort
    coach_list = f.coach_read()
    old_list = []
    new_list = []

    for coach in coach_list:
        old_list.append(coach[key_name])

    # sort items of list
    while old_list:
        tmp = old_list[0]
        try:
            tmp = int(tmp)
            for i in old_list:
                if i > tmp:
                    tmp = i
        except:
            for i in old_list:
                if i < tmp:
                    tmp = i
        new_list.append(tmp)
        old_list.remove(tmp)

    print("\n\t★★★ Here the results ★★★\n")
    # display records after sort
    for sort_item in new_list:
        for coach in coach_list:
            if sort_item == coach[key_name]:
                print_records(coach)
                break


def modify_coach(num, coach):  # modify coaches
    try:
        num = int(num)
        if num == 1:
            coach["Name"] = input("\n\tPlease Enter Name: ")
        elif num == 2:
            coach["Date Joined"] = input(
                "\n\tPlease Enter Date Joined: ")
        elif num == 3:
            coach["Date Terminated"] = input(
                "\n\tPlease Enter Date Terminated: ")
        elif num == 4:
            while 1:
                try:
                    coach["Horly Rate (RM/h)"] = int(
                        input("\n\tPlease Enter Horly Rate (RM/h): "))
                    break
                except:
                    print("\n\tPlease Enter the number")
        elif num == 5:
            coach["Phone"] = input("\n\tPlease Enter Phone: ")
        elif num == 6:
            coach["Adress"] = input(
                "\n\tPlease Enter Adress: ")
        elif num == 7:
            # Check whether the input of Sport center code exits or not
            while 1:
                sport_center_code = input("\tSport Center Code: ")
                sport_center_list = f.sport_center_read()
                for sport_center in sport_center_list:
                    if sport_center == sport_center_code:
                        coach["Sport Center Code"] = sport_center_code
                        coach["Sport Center Name"] = sport_center["Sport Center Name"]
                print("\n\tThere is no", sport_center_code, "in this system")
        elif num == 8:
            # Check whether the input of sport code exits or not
            while 1:
                sport_code = input("\tSport Code: ")
                sport_list = f.sport_read()
                for sport_center in sport_list:
                    if sport_center == sport_code:
                        coach["Sport Code"] = sport_code
                        coach["Sport Name"] = sport_center["Sport Name"]
                print("\n\tThere is no", sport_code, "in this system")
    except:
        print("\n\tWrong Input")


def date_time(coach):  # get input of  schedule
    while 1:
        try:
            year = int(input("\tYear: "))
            month = int(input("\tMonth: "))
            day = int(input("\tDay: "))
            start_hour = int(input("\tStart Time (Hour): "))
            start_minute = int(input("\tStart Time (Minute): "))
            end_hour = int(input("\tEnd Time (Hour): "))
            end_minute = int(input("\tEnd Time (Minute): "))

            start = d.datetime(year, month, day, start_hour, start_minute)
            end = d.datetime(year, month, day, end_hour, end_minute)

            if(start < end) and date_comparison(coach, start):
                date = d.datetime.strptime(
                    str(start), '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
                start_time = d.datetime.strptime(
                    str(start), '%Y-%m-%d %H:%M:%S').strftime('%H:%M')
                end_time = d.datetime.strptime(
                    str(end), '%Y-%m-%d %H:%M:%S').strftime('%H:%M')
                return date, start_time, end_time
            else:
                print("\n\tYour Date and Time is not correct. Pleaset try again.")
                continue

        except:
            print("\n\tWrong Input. Please try again.")
            continue


# Validate the schedule between date joined and date terminated
def date_comparison(coach, start):
    # Coach Date Joined
    date_joined = coach["Date Joined"]
    jdatetime = d.datetime.strptime(date_joined, '%Y/%m/%d')
    jdate = d.date(jdatetime.year, jdatetime.month, jdatetime.day)

    # Coach Date Terminated
    date_terminated = coach["Date Terminated"]
    tdatetime = d.datetime.strptime(date_terminated, '%Y/%m/%d')
    tdate = d.date(tdatetime.year, tdatetime.month, tdatetime.day)

    # Schedule Date
    sdatetime = d.datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S')
    sdate = d.date(sdatetime.year, sdatetime.month, sdatetime.day)

    if sdate >= jdate and sdate <= tdate:
        return True
    else:
        return False


def check_date(coach):  # validate date joined and date terminated
    while 1:
        try:
            joined_year = int(input("\tDate Joined (Year): "))
            joined_month = int(input("\tDate Joined (Month): "))
            joined_day = int(input("\tDate Joined (Day): "))
            terminated_year = int(input("\tDate Terminated (Year): "))
            terminated_month = int(input("\tDate Terminated (Month): "))
            terminated_day = int(input("\tDate Terminated (Day): "))

            date_joined = d.date(joined_year, joined_month, joined_day)
            date_terminated = d.date(
                terminated_year, terminated_month, terminated_day)

            # check whether date joined is ealier than date terminated
            if date_joined < date_terminated:
                coach["Date Joined"] = d.datetime.strptime(
                    str(date_joined), '%Y-%m-%d').strftime('%Y/%m/%d')
                coach["Date Terminated"] = d.datetime.strptime(
                    str(date_terminated), '%Y-%m-%d').strftime('%Y/%m/%d')
                return
            else:
                print("\n\tYour Date is not correct. Pleaset try again.")
                continue

        except:
            print("\n\tWrong Input. Please try again.")
            continue
