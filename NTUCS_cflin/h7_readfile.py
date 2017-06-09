file = open('stores_old.csv', 'r', encoding='UTF-8')
for line in file.readlines():
    print(line, end='')
    file.close()
