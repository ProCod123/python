from models import adding_record, student_score, disciplinces, student_exist
import views

file_path = 'journal.txt'

def run():
    action()


def action():
    user_choice = views.who_is()
    if user_choice == '1':
        surname = views.get_sername()
        for discipline in disciplinces(file_path):
            if student_exist(surname, file_path) > 0:
                student_score(surname, discipline, file_path)
            else:
                print('Записей с такой фамилией в журнале нет!')    
    elif user_choice == '2':
        data = views.get_info()
        adding_record(data, file_path)
    else:
        print('Вы ввели некорректные данные!')
