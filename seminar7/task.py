
#with open("spravochnik.txt", "r") as f:
#    text = f.readlines()
#    compressed = count_symbol(text[0])

def get_info():
    questions = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    answers = [input(f'{i}: ') for i in questions] 
    return answers
get_info()



with open("spravochnik.txt", "a", encoding='utf-8') as f:
    print('Запись выполнена!')
    #Фамилия           |Имя             |Отчество          |  Номер телефона  |    Описание    |
    last_name = 'Семенов'
    name = 'Валентин'
    patronymic = 'Сергеевич'
    phone = '89182453301'
    description = 'раб'
    sep1 = (18 - len(last_name)) * ' '
    sep2 = (16 - len(name)) * ' '
    sep3 = (18 - len(patronymic)) * ' '
    sep4 = (18 - len(phone)) * ' '
    sep5 = (18 - len(phone)) * ' '

    f.write(f'{last_name}{sep1}|{name}{sep2}|{patronymic}{sep3}|{phone}{sep4}|{description}{sep5}|\n')



