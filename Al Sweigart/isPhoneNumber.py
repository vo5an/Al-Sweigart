def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Позвони мне завтра по номеру 415-555-1011, ' \
          '415-555-9999 - это телефонный номер моего офиса.'
for i in range(len(message)):
    chuck = message[i:i+12]
    if isPhoneNumber(chuck):
        print('Найденный телефонный номер: ' + chuck)
print('Готово')