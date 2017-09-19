a, b, maxshare = int(input()), int(input()), int()
i = int(1)
if a < b:
    a, b = b, a
while i <= a:
    if a%i == 0 and b%i == 0:
        maxshare = i
    i += 1
print(int(a*b/maxshare))