Year = int(input())
if 1900 <= Year <= 3000:
 print('Високосный' if not Year%400 or not Year%4 and Year%100 else 'Обычный')