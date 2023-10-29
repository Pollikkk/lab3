# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, razd=','):
    both = []
    partic_1 = str1.split(razd)
    partic_2 = str2.split(razd)

    for part_1 in partic_1:
        for part_2 in partic_2:
            if part_1 == part_2:
                both.append(part_1)
    both.sort()
    return(both)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))