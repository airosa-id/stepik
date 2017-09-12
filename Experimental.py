programmers = int(input())
swarm_progs = int()
last = str()
if 100 <= programmers < 999:
    swarm_progs = programmers % 100
    if swarm_progs > 20:
        swarm_progs = programmers % 10

if 20 < programmers < 100:
    swarm_progs = programmers % 10

if programmers == 1 or swarm_progs == 1:
    last = ""
elif (2 <= programmers <= 4) or (2 <= swarm_progs <= 4):
    last = "а"
elif (5 <= programmers <= 20) or (programmers == 0) or (programmers == 1000) or (5 <= swarm_progs <= 20) or (swarm_progs == 0):
    last = "ов"

print (swarm_progs)
print (str(programmers) +" программист"+ str(last))