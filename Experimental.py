a = int(input())
b = int(input())
maxshare = int()
i = int(1)

while i <= 9:
    if a%i == 0 and b%i == 0:
        maxshare = i
    i += 1

print(a*b/maxshare)