# 1. Remove Even Numbers: Write a function that takes an array of integers as input and
# removes all the even numbers from the array, returning a new array with only the 
# odd numbers. 

start, end = 2, 20
for numbers in range (start, end + 1):
    if numbers % 2 != 0:
        print( numbers, end = " ")

start, end = 4, 19
 

# 2. Array Intersection: Write a function that takes two arrays of integers as input and returns a 
# new array containing the intersection of the two arrays

def find_array_intersection(arr1, arr2):
    intersection = [value for value in arr1 if value in arr2]
    return intersection

array1 = [6, 7, 8, 9]
array2 = [2, 3, 4, 5]
answer = find_array_intersection(array1, array2)
print(answer)


# 3. Array Flattening: Write a function that takes a nested array of integers as input and returns
# a new array with all the elements flattened (i.e., all nested arrays are merged into a single array).
# For example, given the input [[1, 2], [3, 4], [5, 6]], the function should return [1, 2, 3, 4, 5, 6].

def find_flattened_array(nested_array):
    flattened = []
    for my_arrays in nested_array:
        for elements in my_arrays:
            flattened.append(elements)
    return flattened
nested_array = [[11, 12], [23, 24], [33, 36]]    
my_answer = find_flattened_array(nested_array)
print(my_answer)    


# 5. Find Missing Number: Write a function that takes an array of integers from 1 to n, with 
# one number missing, and returns the missing number. For example, given the input 
# [1, 2, 3, 5], the function should return 4.

def find_missing_number(my_nums):
    n = len(my_nums) + 1
    final_sum = n * (n + 1) // 2
    array_sum = sum(my_nums)
    missing_number = final_sum - array_sum
    return missing_number
numbera = [4, 5, 6, 7, 8]
result = find_missing_number(numbera)
print(result)