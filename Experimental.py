a,b,c= [int(input()) for i in range(3)]

max = a
if a <= b:
    min = a
    max = b
    if  c <= a:
        min = c
        mid = a
    elif c >= b:
        max = c
        mid = b
    else:
        mid = c
else:
    min = b
    max = a
    if c <= b:
        min = c
        mid = b
    elif c >= a:
        max = c
        mid = a
    else:
        mid = c
print (str(max) + '\n' + str(min) +'\n' + str(mid))