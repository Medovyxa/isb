import os
from config_data import CONFIG_PATH, SUBSTITUTION_DICT
from helpers import read_json, read_text


def decrypt_message(text):
    decoded_text = ""
    for char in text:
        decoded_text += SUBSTITUTION_DICT.get(char, char)  
    return decoded_text


def run_decoder():
    config = read_json(CONFIG_PATH)
    if config is None:
        return 

    
    input_file_path = os.path.join(config["folder"], config["input_file"])
    output_file_path = os.path.join(config["folder"], config["output_file"])

    
    if not os.path.exists(input_file_path):
        print("Файл не найден:", input_file_path)
        return

    text = read_text(input_file_path)
    if text == "":
        print("Файл пуст:", input_file_path)
        return

    decoded_text = decrypt_message(text)

    
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(decoded_text)
    print("Расшифрованный текст сохранён в", output_file_path)

if __name__ == "__main__":
    run_decoder()