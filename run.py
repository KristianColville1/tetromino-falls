from tetromino.tetromino.console import clear_console
import time
grid = []
# for y rows insert x columns
for _ in range(23):
    grid.append([])
for i in grid:
    for _ in range(15):
        i.append([0])

for a in grid:
    for b in a:
        if a == 7:
            a.append(1)
zerostring = ''
for twoD in grid:
    for oneD in twoD:
        for val in oneD:
            if val == 0:
                zerostring+='\033[6;30;47m  \033[0m'
            if val == 1:
                zerostring+='\033[6;30;43m  \033[0m'
    zerostring+='\n'

counter = 0
new_line = '\n'
while True:
    new_line = '\n'
    clear_console()
    print((counter * new_line) + '\033[6;30;43m      \033[0m')
    counter += 1
    if counter == 20:
        counter = 0
        new_line = ''
    time.sleep(1)