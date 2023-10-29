# Выполнение первого задания
def stock(stocklist, product):
    for i in range(len(stocklist)):
        if product == stocklist[i]:
            return i
    return None

list1 = ["Картошка", "Морковь", "Чебурек", "Ваз2107", "Чебурек"]
print(stock(list1, "Чебурек"))
print(stock(list1, "Картошка"))
print(stock(list1, "Бентли"))
