bilet = int(input())
bil1,bil2,bil3,bil4,bil5,bil6, = int(),int(),int(),int(),int(),int()
if bilet <= 999999:
    bil6 = bilet % 10
    next_num= bilet // 10
    bil5 = next_num % 10
    next_num= next_num // 10
    bil4 = next_num % 10
    next_num= next_num // 10
    bil3 = next_num % 10
    next_num= next_num // 10
    bil2 = next_num % 10
    next_num= next_num // 10
    bil1 = next_num % 10
    next_num= next_num // 10
    if bil1+bil2+bil3 == bil4+bil5+bil6:
        print('Счастливый')
    else:
        print('Обычный')