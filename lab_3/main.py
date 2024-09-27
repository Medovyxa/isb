import argparse
import json
import os
from algorithms.hybrid import hybrid_encrypt, hybrid_decrypt
from algorithms.asymmetric import generate_keys
from cryptography.hazmat.primitives import serialization

def main():
    # Загружаем настройки
    with open('settings.json') as json_file:
        settings = json.load(json_file)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', action='store_true', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', action='store_true', help='Запускает режим дешифрования')

    args = parser.parse_args()

    if args.generation:
        print("Генерация ключей...")
        private_key, public_key = generate_keys(settings['public_key'], settings['private_key'])
        print("Ключи успешно сгенерированы и сохранены.")

    elif args.encryption:
        with open(settings['public_key'], 'rb') as f:
            public_key_bytes = f.read()
            public_key = serialization.load_pem_public_key(public_key_bytes)

        print("Шифрование данных...")
        with open(settings['initial_file'], 'rb') as f:
            text = f.read()

        symmetric_key = os.urandom(32)  
        encrypted_text, encrypted_key, iv = hybrid_encrypt(text, symmetric_key, public_key)

        with open(settings['encrypted_file'], 'wb') as f:
            f.write(encrypted_text)

        with open(settings['symmetric_key'], 'wb') as f:
            f.write(encrypted_key)

        print("Данные успешно зашифрованы и сохранены.")

    elif args.decryption:
        print("Дешифрование данных...")
        with open(settings['encrypted_file'], 'rb') as f:
            encrypted_text = f.read()

        with open(settings['symmetric_key'], 'rb') as f:
            encrypted_key = f.read()

        with open(settings['private_key'], 'rb') as f:
            private_key_bytes = f.read()
            private_key = serialization.load_pem_private_key(private_key_bytes, password=None)

        decrypted_text = hybrid_decrypt(encrypted_text, encrypted_key, iv, private_key)

        with open(settings['decrypted_file'], 'wb') as f:
            f.write(decrypted_text)

        print("Данные успешно расшифрованы и сохранены.")

if __name__ == "__main__":
    main()