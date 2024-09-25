def caesar_cipher(text, shift):
    result = ""
    for i in text:
        if i.isalpha():
            base = ord('а') if i.islower() else ord('А')
            result += chr(base + (ord(i) - base + shift) % 32)
        else:
            result += i
    return result

def generate_shift_key():
    return 5