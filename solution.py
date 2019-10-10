file = open('input.txt', 'r', encoding='utf8')
pupils = []
for line in file:
    temp = line.split()
    temp[0] = temp[0].replace('\ufeff', '')
    temp2 = (temp[0], temp[1], temp[3])
    pupils.append(temp2)
pupils.sort(key=lambda x: x[0])
file2 = open('output.txt', 'w', encoding='utf8')
for line in pupils:
    print(' '.join(map(str, line)), file=file2)
file.close()
file2.close()
