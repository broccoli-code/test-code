# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(str1_, str2_, n=","):
    list_words = set(str1_.split(n))
    list_wordssecond = set(str2_.split(n))
    common_list = list_words.intersection(list_wordssecond)
    common_list = list(common_list)
    common_list.sort()
    return (common_list)

print(find_common_participants(participants_first_group, participants_second_group, n="|"))