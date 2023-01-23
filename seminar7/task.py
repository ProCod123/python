def action():
    user_choice = input('Выберите действие: \n'
           '1 - показать все записи в справочнике \n' 
           '2 - добавить запись\n')
    if user_choice == '1':
        all_records('spravochnik.txt')
    elif user_choice == '2':
        adding_record("spravochnik.txt", "second_format.txt" )
    else:
        print('Вы ввели некорректные данные!')    

def get_info():
    questions = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    answers = [input(f'{i}: ') for i in questions] 
    return answers

def all_records(file):
    with open(file, "r", encoding='utf-8') as f:
        for line in f:
            print(line, end = '')

def adding_record(file_path1, file_path2):
        answers = get_info()
        if answers[3].isdigit() == True:
            first_format(answers, file_path1)
            second_format(answers, file_path2)
            print('Запись добавлена!')
        else:
            print('Запись данных не выполнена! ' 
                'Номер телефона должен состоять из цифр')


def first_format(data, file_path):
    with open(file_path, "a", encoding='utf-8') as f:
        record = ''
        for item in data:
            record += item + (16 - len(item)) * ' ' + '|'  
        spliter = '-' * 85      
        f.write(record + '\n' + spliter + '\n')

def second_format(data, file_path):
    with open(file_path, "a") as f:
        record = ''
        for i in data:
            record += i + '\n'
        spliter = '-' * 16
        f.write(record + spliter + '\n')                

action()