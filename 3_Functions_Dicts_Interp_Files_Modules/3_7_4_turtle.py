n = int(input())
commands = []
x = 0
y = 0
for i in range(n):
    commands.append(input())
    d = commands[i].split(' ')
    if d[0] == 'север':
        y += int(d[1])
    if d[0] == 'юг':
        y -= int(d[1])
    if d[0] == 'восток':
        x += int(d[1])
    if d[0] == 'запад':
        x -= int(d[1])
print(x,y)