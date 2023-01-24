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
        spliter = '-' * 85
        f.write(record + '\n' + spliter + '\n')


def second_format(data, file_path):
    with open(file_path, "a", encoding='utf-8') as f:
        record = ''
        for i in data:
            record += i + '\n'
        spliter = '-' * 16
        f.write(record + spliter + '\n')
