list1 = []
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if x + y + z != 2:
                list1.append([x, y, z])
print(list1)


