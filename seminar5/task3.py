def count_symbol(text):
    count = 0
    result = ''
    for i in range(len(text)):
        symbol = text[i]
        if i < len(text) - 1:
            if symbol != text[i + 1]:
                count += 1
                result += str(count) + symbol
                count = 0
                continue
            else:
                count += 1
        elif i == len(text) - 1:
            if symbol != text[i]:
                symbol = text[i]
                count += 1
                result += str(count) + symbol
            else:
                count += 1
                result += str(count) + symbol
    return result


def unzip(compressd_text):
    unzip_text = ''
    for i in range(1, len(compressd_text), 2):
        unzip_text += compressd_text[i] * int(compressd_text[i - 1]) 
    return unzip_text


with open("text.txt", "r") as f:
    text = f.readlines()
    compressed = count_symbol(text[0])

with open("text.txt", "w") as f:
    print('Сжатие выполнено!')
    f.write(text[0] + '\n' + compressed + '\n' + unzip(compressed))
