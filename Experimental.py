Year = int(input())
if 1900 <= Year <= 3000:
    if not((((Year % 4)==0) and not((Year % 100)==0)) or ((Year % 400)==0)):
        print ('Високосный')
    else:
        print ('Обычный')
else:
    print ('Ошибка диапазона')