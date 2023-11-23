list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
list2 = []

for i in list:
    if i not in list2:
        list2.append(i)

print(list2)
