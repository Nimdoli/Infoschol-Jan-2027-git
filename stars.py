
import time

rows = 4
for n in range (1, rows + 1):
    spaces = rows - n
    stars = 2 * n - 1
    print(((" " * spaces + "*" * stars) + " " * spaces)*10)
    time.sleep(1)

rows = 4
for n in range (rows, 0, -1):
    spaces = rows - n
    stars = 2 * n - 1
    print(((" " * spaces + "*" * stars) + " " * spaces)*10)
    time.sleep(1)

