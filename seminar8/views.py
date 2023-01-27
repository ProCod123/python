def who_is():
    user_choice = input('Кто вы: \n'
                        '1 - студент \n'
                        '2 - преподаватель\n')
    return user_choice

def get_sername():
    sername = input('Введите свою фамилию: ')
    return sername
    

def get_info():
    questions = ['Предмет', 'Фамилия', 'Имя', 'Оценка']
    data = [input(f'{i}: ') for i in questions]
    return data


def all_records(file):
    with open(file, "r", encoding='utf-8') as f:
        for line in f:
            print(line, end='')

#def list_scores(sername):
#    for discipline in disciplinces():
#        for sername in all_students():
#            student_score(sername, discipline)


#list_scores('Иванов')          