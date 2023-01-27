def who_is():
    user_choice = input('Кто вы: \n'
                        '1 - студент \n'
                        '2 - преподаватель\n')
    return user_choice

def get_sername():
    sername = input('Введите свою фамилию: ')
    return sername
    

def get_info():
    questions = ['Предмет', 'Фамилия', 'Оценка']
    data = [input(f'{i}: ') for i in questions]
    return data

     