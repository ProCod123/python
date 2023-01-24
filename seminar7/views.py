def what_do():
    user_choice = input('Выберите действие: \n'
                        '1 - показать все записи в справочнике \n'
                        '2 - добавить запись\n')
    return user_choice


def get_info():
    questions = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    data = [input(f'{i}: ') for i in questions]
    return data


def all_records(file):
    with open(file, "r", encoding='utf-8') as f:
        for line in f:
            print(line, end='')
