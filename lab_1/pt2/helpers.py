import json


def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        print("Ошибка чтения файла настроек")
        return None


def read_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        print("Не удалось прочитать файл:", file_path)
        return ""