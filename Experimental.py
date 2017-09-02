A = int(input ())
B = int(input ())
H = int(input ())

if H < A:
    print('Недосып')
elif A <= H <= B:
    print('Это нормально')
elif H > B:
    print('Пересып')
elif A > B:
    print('error')