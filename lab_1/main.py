import os
import json
from caesar_cipher import caesar_cipher, generate_shift_key

def load_json(file_path: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return {}

def save_json(data: dict, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main() -> None:
    
    config = load_json("texts/config.json")
    
    
    with open(os.path.join(config["directory"], config["source_text"]), "r", encoding="utf-8") as file:
        text = file.read()

    
    shift_key = generate_shift_key()
    encrypted_text = caesar_cipher(text, shift_key)

    
    with open(os.path.join(config["directory"], config["encrypted_text"]), "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    
    save_json({"shift_key": shift_key}, os.path.join(config["directory"], config["key_file"]))

    print("Текст успешно зашифрован и сохранён.")

if __name__ == "__main__":
    main()