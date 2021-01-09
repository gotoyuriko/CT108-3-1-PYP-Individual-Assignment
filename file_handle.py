import json


def admin_login_read():
    with open("admin_login.txt") as adminf:
        admin_data = adminf.read()
        admin_dict = json.loads(admin_data)

    return admin_dict


def coach_read():
    with open("coach.txt") as coachf:
        coach_data = coachf.read()
        coach_list = json.loads(coach_data)

    return coach_list


def coach_write(coach_list):
    with open("coach.txt", "w") as coachf:
        encode_coach = json.dumps(coach_list)
        coachf.write(encode_coach)


def sport_center_read():
    with open("sport_center.txt") as sportcenterf:
        sport_center_data = sportcenterf.read()
        sport_center_list = json.loads(sport_center_data)

    return sport_center_list


def sport_read():
    with open("sport.txt") as sportf:
        sport_data = sportf.read()
        sport_list = json.loads(sport_data)

    return sport_list


def sport_write(sport_list):
    with open("sport.txt", "w") as sportf:
        encode_sport = json.dumps(sport_list)
        sportf.write(encode_sport)


def student_read():
    with open("student.txt") as studentf:
        student_data = studentf.read()
        student_list = json.loads(student_data)

    return student_list


def student_write(student_list):
    with open("student.txt", "w") as studentf:
        encode_student = json.dumps(student_list)
        studentf.write(encode_student)


def schedule_read():
    with open("schedule.txt") as schedulef:
        schedule_data = schedulef.read()
        schedule_list = json.loads(schedule_data)

    return schedule_list


def schedule_write(schedule_list):
    with open("schedule.txt", "w") as schedulef:
        encode_schedule = json.dumps(schedule_list)
        schedulef.write(encode_schedule)


def rating_read():
    with open("rating.txt") as ratingf:
        rating_data = ratingf.read()
        rating_list = json.loads(rating_data)

    return rating_list


def rating_write(rating_list):
    with open("rating.txt", "w") as ratingf:
        encode_rating = json.dumps(rating_list)
        ratingf.write(encode_rating)


def feedback_read():
    with open("feedback.txt") as feedbackf:
        feedback_data = feedbackf.read()
        feedback_list = json.loads(feedback_data)

    return feedback_list


def feedback_write(feedback_list):
    with open("feedback.txt", "w") as feedbackf:
        encode_rating = json.dumps(feedback_list)
        feedbackf.write(encode_rating)
