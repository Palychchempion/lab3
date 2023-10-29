 # Выполнение второго задания
def group(group1, group2):
    group1 = group1.split(",")
    group2 = group2.split(",")
    group3 = []
    for i in group1:
        for j in group2:
            if i == j:
                group3.append(i)
    group3.sort()
    return group3


Students = "Дамир,Марвин,Данил,Илюха,Никита"
Sportsmens = "Дамир,Олег,Никита"
print(group(Students, Sportsmens))
