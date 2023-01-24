from models import adding_record
import views


def run():
    action()


def action():
    user_choice = views.what_do()
    if user_choice == '1':
        views.all_records('spravochnik.txt')
    elif user_choice == '2':
        data = views.get_info()
        adding_record(data, "spravochnik.txt", "second_format.txt")
    else:
        print('Вы ввели некорректные данные!')
