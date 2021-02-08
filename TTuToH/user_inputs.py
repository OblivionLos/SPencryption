from TTuToH.coder import *

def input_encode():
    data = ""
    while True:
        data = input("Введите открытый текст (максимум 80 символов): ")
        if len(data) <= 80:
            if len(data) % 2 != 0:
                data += " "
            break
        else:
            print("Введено некорректное значение")

    print("")
    print("Вы ввели: ")
    print(data)
    print("В шестнадцатеричном представлении: ")
    data = norm_to_hex(data)
    print(data)
    print("")
    print("Ваше зашифрованное сообщение: ")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(encode(data))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")


def input_decode():
    data = input("Введите текст в зашифрованном виде (в шестнадцатеричном виде): ")
    print("")
    print("Вы ввели: ")
    print(data)
    print("В шестнадцатеричном представлении: ")
    print(decode(data)[0])
    print("")
    print("Ваше расшифрованное сообщение: ")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(decode(data)[1])
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")

