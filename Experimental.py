'''
Напишите программу, принимающую на вход целое число, которая выводит True,
если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False
в противном случае (регистр символов имеет значение).

'''
a = float(input())
b = float(input())
operation = input('+,-,/,*,mod,pow,div')
if operation == '+':
    print (a+b)
elif operation == '-':
    print (a-b)
elif operation == '/':
    if b == 0:
        print ('Деление на 0!')
    else:
        print (a/b)
elif operation == '*':
    print (a*b)
elif operation == 'mod':
    print (a//b)
elif operation == 'pow':
    print (a**b)
elif operation == 'div':
    print (a%b)

