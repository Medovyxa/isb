import random

# Русский алфавит, включая пробел
alphabet = ' АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# Частотный индекс появления букв русского алфавита
frequency_index = {
    ' ': 0.128675, 'О': 0.096456, 'И': 0.075312, 'Е': 0.072292, 'А': 0.064841, 'Н': 0.061820, 
    'Т': 0.061619, 'С': 0.051953, 'Р': 0.040677, 'В': 0.039267, 'М': 0.029803, 'Л': 0.029400, 
    'Д': 0.026983, 'Я': 0.026379, 'К': 0.025977, 'П': 0.024768, 'З': 0.015908, 'Ы': 0.015707, 
    'Ь': 0.015103, 'У': 0.013290, 'Ч': 0.011679, 'Ж': 0.010673, 'Г': 0.009867, 'Х': 0.008659, 
    'Ф': 0.007249, 'Й': 0.006847, 'Ю': 0.006847, 'Б': 0.006645, 'Ц': 0.005034, 'Ш': 0.004229, 
    'Щ': 0.003625, 'Э': 0.002416, 'Ъ': 0.000000
}

# Генерация шифра подстановки с учётом частотного индекса
def generate_frequency_based_key():
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    
    # Сортировка алфавита и частотных данных
    sorted_alphabet = sorted(frequency_index, key=frequency_index.get, reverse=True)
    return dict(zip(sorted_alphabet, shuffled_alphabet))

# Функция шифрования текста с использованием шифра подстановки
def encrypt(text, key):
    return ''.join([key.get(char, char) for char in text.upper()])

# Чтение исходного текста из файла
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

# Запись текста в файл
def write_text(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)

# Основная функция шифрования
def main():
    # Исходный текст (например, возьмём текст из файла source_text.txt)
    source_text = read_text('source_text.txt')

    # Генерация ключа подстановки на основе частотного анализа
    key = generate_frequency_based_key()

    # Шифрование текста
    encrypted_text = encrypt(source_text, key)

    # Запись результатов в файлы
    write_text('encrypted_text.txt', encrypted_text)

    # Запись ключа в файл в виде соответствий символов
    with open('substitution_key.txt', 'w', encoding='utf-8') as f:
        for original_char, encrypted_char in key.items():
            f.write(f'{original_char} -> {encrypted_char}\n')

    print('Шифрование завершено. Файлы сохранены.')

if __name__ == '__main__':
    main()