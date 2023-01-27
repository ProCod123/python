def adding_record(data, file_path):
    if data[2].isdigit() is True:
        with open(file_path, "a", encoding='utf-8') as f:
            record = ''
            for i in data:
                record += i + '|'
            f.write(record + '\n')
        print('Запись добавлена!')
    else:
        print('Запись данных не выполнена! '
              'Вместо оценки введен текст')


def student_score(surname, discipline, file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        line = file.readline()
        output = discipline + ': '
        count = 0
        while line:
            if surname in line and discipline in line:
                list_data = line.split('|')
                output += ' ' + list_data[-2]
                count += 1
            line = file.readline()      
    print(output)



def student_exist(surname, file_path): # Проверка на наличие фамилии в журнале
    with open(file_path, "r", encoding='utf-8') as file:
        line = file.readline()
        count = 0
        while line:
            if surname in line:
                count += 1
            line = file.readline()      
    return count


def disciplinces(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        line = file.readline()
        disciplinces = []
        while line:
            list_data = line.split('|')
            disciplinces.append(list_data[0])
            line = file.readline()
    unic_discipline = set(disciplinces)
    return unic_discipline 







