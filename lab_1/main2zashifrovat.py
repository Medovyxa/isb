from collections import Counter

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

# Сортировка частотного индекса русского алфавита
sorted_russian_frequency = sorted(frequency_index, key=frequency_index.get, reverse=True)

# Подсчёт частоты символов в зашифрованном тексте
def calculate_frequency(text):
    counter = Counter(text)
    total = sum(counter.values())
    frequency = {char: count / total for char, count in counter.items()}
    return frequency

# Сортировка символов по частоте появления
def sort_by_frequency(frequency_dict):
    return sorted(frequency_dict, key=frequency_dict.get, reverse=True)

# Генерация ключа дешифровки на основе частотного анализа
def generate_decryption_key(encrypted_text):
    encrypted_frequency = calculate_frequency(encrypted_text)
    sorted_encrypted_chars = sort_by_frequency(encrypted_frequency)

    # Сопоставляем символы зашифрованного текста с наиболее частыми символами русского алфавита
    decryption_key = dict(zip(sorted_encrypted_chars, sorted_russian_frequency))
    return decryption_key

# Дешифровка текста
def decrypt(text, key):
    return ''.join([key.get(char, char) for char in text])

# Чтение текста из файла
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

# Запись текста в файл
def write_text(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)

# Основная функция дешифровки
def main():
    # Чтение зашифрованного текста из файла
    encrypted_text = read_text('cod7.txt')

    # Генерация ключа дешифровки
    decryption_key = generate_decryption_key(encrypted_text)

    # Дешифровка текста
    decrypted_text = decrypt(encrypted_text, decryption_key)

    # Запись результатов в файлы
    write_text('decrypted_text.txt', decrypted_text)

    # Запись ключа в файл
    with open('decryption_key.txt', 'w', encoding='utf-8') as f:
        for encrypted_char, decrypted_char in decryption_key.items():
            f.write(f'{encrypted_char} -> {decrypted_char}\n')

    print('Дешифровка завершена. Файлы сохранены.')

if __name__ == '__main__':
    main()