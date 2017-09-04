Year = int(input())
if not(((Year % 4)==0) and not((Year % 100)==0)):
    print ('True',Year%4,Year//100)
else:
    print ('False',Year%4,Year//100)
 dd