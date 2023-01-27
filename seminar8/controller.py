from models import adding_record, student_score, disciplinces, all_students
import views


def run():
    action()


def action():
    user_choice = views.who_is()
    if user_choice == '1':
        surname = views.get_sername()
#        for item in disciplinces():
#            student_score(surname, item)
        for discipline in disciplinces():
            for surname in all_students():
                student_score(surname, discipline)
    elif user_choice == '2':
        data = views.get_info()
        adding_record(data, "spravochnik.txt", "second_format.txt")
    else:
        print('Вы ввели некорректные данные!')
