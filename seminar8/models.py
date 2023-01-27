def adding_record(data, file_path1, file_path2):
    if data[3].isdigit() is True:
        first_format(data, file_path1)
        second_format(data, file_path2)
        print('Запись добавлена!')
    else:
        print('Запись данных не выполнена! '
              'Номер телефона должен состоять из цифр')


def first_format(data, file_path):
    with open(file_path, "a", encoding='utf-8') as f:
        record = ''
        for item in data:
            record += item + (16 - len(item)) * ' ' + '|'
        spliter = '-' * 68
        f.write(record + '\n' + spliter + '\n')


def second_format(data, file_path):
    with open(file_path, "a", encoding='utf-8') as f:
        record = ''
        for i in data:
            record += i + '|'
        f.write(record + '\n')


def student_score(surname, discipline):
    with open("second_format.txt", "r", encoding='utf-8') as file:
        line = file.readline()
        output = discipline + ' ' + surname + ':'
        while line:
            if surname in line and discipline in line:
                list_data = line.split('|')
                output += ' ' + list_data[-2]
            line = file.readline()      
    print(output)



def disciplinces():
    with open("second_format.txt", "r", encoding='utf-8') as file:
        line = file.readline()
        disciplinces = []
        while line:
            list_data = line.split('|')
            disciplinces.append(list_data[0])
            line = file.readline()
    unic_discipline = set(disciplinces)
    return unic_discipline 


disciplinces()


def all_students():
    with open("second_format.txt", "r", encoding='utf-8') as file:
        line = file.readline()
        students = []
        while line:
            list_data = line.split('|')
            students.append(list_data[1])
            line = file.readline()
    unic_students = set(students)
    return unic_students


all_students()



