def encrypt_ru():
    print('Введите шаг сдига')
    step = int(input())
    if step >= 32:
        step %= 32
    print('Введите текст')
    s = input()
    new_s = ''
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if s[i].isupper() == True:
                if ord(s[i]) + step > 1071:
                    new_s += chr(ord(s[i]) + step - 1071 + 1039)
                else:
                    new_s += chr(ord(s[i]) + step)
            else:
                if ord(s[i]) + step > 1103:
                    new_s += chr(ord(s[i]) + step - 1103 + 1071)
                else:
                    new_s += chr(ord(s[i]) + step)
        else:
            new_s += s[i]
    return new_s

def encrypt_en():
    print('Введите шаг сдига')
    step = int(input())
    if step >= 26:
        step %= 26
    print('Введите текст')
    s = input()
    new_s = ''
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if s[i].isupper() == True:
                if ord(s[i]) + step > 90:
                    new_s += chr(ord(s[i]) + step - 90 + 64)
                else:
                    new_s += chr(ord(s[i]) + step)
            else:
                if ord(s[i]) + step > 122:
                    new_s += chr(ord(s[i]) + step - 122 + 96)
                else:
                    new_s += chr(ord(s[i]) + step)
        else:
            new_s += s[i]
    return new_s

def decrypt_ru():
    print('Введите шаг сдига')
    step = int(input())
    if step >= 32:
        step %= 32
    print('Введите текст')
    s = input()
    new_s = ''
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if s[i].isupper() == True:
                if ord(s[i]) - step < 1040:
                    new_s += chr(ord(s[i]) - step + 32)
                else:
                    new_s += chr(ord(s[i]) - step)
            else:
                if ord(s[i]) - step < 1072:
                    new_s += chr(ord(s[i]) - step + 32)
                else:
                    new_s += chr(ord(s[i]) - step)
        else:
            new_s += s[i]
    return new_s

def decrypt_en():
    print('Введите шаг сдига')
    step = int(input())
    if step >= 26:
        step %= 26
    print('Введите текст')
    s = input()
    new_s = ''
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if s[i].isupper() == True:
                if ord(s[i]) - step < 65:
                    new_s += chr(ord(s[i]) - step + 26)
                else:
                    new_s += chr(ord(s[i]) - step)
            else:
                if ord(s[i]) - step < 97:
                    new_s += chr(ord(s[i]) - step + 26)
                else:
                    new_s += chr(ord(s[i]) - step)
        else:
            new_s += s[i]
    return new_s

print('Здравсвуйте, эта программа может шифровать и дешифровать текст в соответствии с алгоритмом Цезаря!')
print('На каком языке ваш текст? (Ru/En)')

language = input()

if language == 'Ru':
    print('Что вы хотите сделать с текстом? (шифровать/дешифровать)')
    answer = input()
    if answer == 'шифровать':
        print(encrypt_ru())
    elif answer == 'дешифровать':
        print(decrypt_ru())
elif language == 'En':
    print('Что вы хотите сделать с текстом? (шифровать/дешифровать)')
    answer = input()
    if answer == 'шифровать':
        print(encrypt_en())
    elif answer == 'дешифровать':
        print(decrypt_en())