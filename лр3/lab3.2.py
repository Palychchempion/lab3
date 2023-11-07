# TODO Напишите функцию find_common_participants

def find_common_participants(first_group,second_group,splitter=','):
    set_1 = set(first_group.split(splitter))
    set_2 = second_group.split(splitter)
    end_list = list(set_1.intersection(set_2))
    end_list.sort()
    return end_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,'|'))

# TODO Проверьте работу функции с разделителем отличным от запятой
