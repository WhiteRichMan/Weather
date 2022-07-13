from hashlib import new


alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqstuvwxyz"
# alphabet = "абвгдеёжзиклмнопрстчхжшзйвщлвзйбдыжюйзьвлзьйзвль"

encrypt = input("Введите своё сообщение: ")
key = int(input("Подалуйста введите ключ (с числом 1-25)"))
encrypt = encrypt.lower()
encrypted = ""

for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print("Ваше зашифрованное сообщение: ", encrypted) 
