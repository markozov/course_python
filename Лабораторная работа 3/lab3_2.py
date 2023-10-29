def find_common_participants(str1, str2, c=','):
    list1_ = str1.split('|')
    list2_ = str2.split('|')
    set_list1 = set(list1_)
    set_list2 = set(list2_)
    intersection_set = set_list1.intersection(set_list2)
    intersection_list = list(intersection_set)
    intersection_list.sort()

    return intersection_list
# TODO Напишите функцию find_common_participants



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
group = find_common_participants(participants_first_group, participants_second_group)
print(group)
# TODO Провеьте работу функции с разделителем отличным от запятой
