#a, b, c, d = int(input()),int(input()),int(input()),int(input())

for i in range (0,9+1):
    for j in range(1, 9 + 1):
        if i == 0:
            print ("  ",end ="")
            print(str(j) + " ", end="")
            continue
        else:
            print (str(i)+" ",  end="")
