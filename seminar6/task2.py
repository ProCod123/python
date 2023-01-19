list_input = [12,'sadf',5643, 'fvdf', 'sdvz', 1236]

digits = list(filter(lambda elem: str(elem).isdigit(), list_input))
letters = list(filter(lambda elem: not str(elem).isdigit(), list_input))

print(f'Цифры: {digits} \nБуквы: {letters}')