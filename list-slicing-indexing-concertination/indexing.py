
# 1. Write a Python function that takes a list lst as input and returns 
# the middle element if the list has an odd number of elements. If the list has an even 
# number of elements, the function should return a new list containing the two middle 
# elements.

def get_middle_element(list):
    my_list = len(list)
    if my_list % 2 == 1:
        middle_index = my_list // 2
        return list[middle_index]
    else:
        middle_index_first = my_list // 2 - 1
        middle_index_second = my_list // 2
        return[list[middle_index_first], list[middle_index_second]]
list = [3, 4, 5, 6, 7]
result = get_middle_element(list)
print(result)

list = [3, 4, 5, 6, 7, 9]
result = get_middle_element(list)
print(result)


# 2. Write a Python function that takes a list lst as input and returns a new 
# list with the elements in reverse order. 
def reverse_list (my_lst):
    return my_lst[::-1]

my_lst = [6, 7, 8, 9]
answer = reverse_list(my_lst)
print(answer)


# 3. Write a Python function that takes two lists, list1 and list2,
# as input and returns a new list that alternates the elements from the two lists. 
# The resulting list should start with the first element of list1, followed by the 
# first element of list2, then the second element of list1, the second element of list2,
# and so on.

def alternate_lists(first_lst, second_lst):
    my_result = []
    for a in range(max(len(first_lst), len(second_lst))):
        if a < len(first_lst):
            my_result.append(first_lst[a])

            if a < len(second_lst):
                my_result.append(second_lst[a])
    return my_result  
first_lst = [2, 6, 4, 1, 2]  
secons_lst = ["q", "u", "w", "r", "a"]  
my_answer = alternate_lists(first_lst, secons_lst)
print(my_answer)      


