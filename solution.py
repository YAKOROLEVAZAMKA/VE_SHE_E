tel = input()


def clean(tel):
    tel = tel.replace('-', '')
    tel = tel.replace('+7', '')
    tel = tel.replace('(', '')
    tel = tel.replace(')', '')
    if len(tel) == 7:
        tel = '495' + tel
    elif len(tel) == 11:
        tel = tel[1:]
    return tel

tel = clean(tel)
book = []
# print(tel)
for i in range(3):
    temp = input()
    temp = clean(temp)
    book.append(temp)
for phone in book:
    if phone == tel:
        print('YES')
    else:
        print('NO')
