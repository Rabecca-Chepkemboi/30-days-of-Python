
# 1. Write a function to check if a given list is sorted in non-decreasing order.d

def sort_non_decreasing_order(numbers):
    for a in range(len(numbers) - 1):
        if numbers[a] > numbers [a + 1]:
            return False
        return True
    
numbers = [6, 7, 8, 3, 2, 4]    
print(sort_non_decreasing_order(numbers))    


# 2. Write a function to remove duplicates from a given list.

def remove_duplicates(my_nums):
    num = set()
    answer = []
    for element in my_nums:
        if element not in num:
            num.add(element)
            answer.append(element)
    return answer

my_nums = [1, 2, 5, 2, 7, 4, 7]
print(remove_duplicates(my_nums))        


# 5. Write a function to merge two sorted lists into a single sorted list.

def merge_two_sorted_lists(list1, list2):
    return sorted(list1 + list2)

list1 = [6, 7, 8, 9]
list2 = [2, 3, 4, 5]
print(merge_two_sorted_lists(list1, list2))