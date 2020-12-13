my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [num for num in my_list if my_list.count(num) < 2]
print(my_new_list)
