# Write a program that prints a pyramid pattern using numbers. The program should prompt the 
# user to enter the height of the pyramid (a positive integer). The pattern should be centered
# and consist of numbers increasing from 1 up to the height of the pyramid. Use the range 
# function to control the number of rows and the values within each row.

def print_pyramid_pattern(length):
    for a in range(1, length + 1):
        print(" " * (length - a), end="")
        for j in range(1, a + 1):
            print(j, end="")

        for j in range(a - 1, 0, -1):
            print(j, end="")  

        print()   
length = 10
print_pyramid_pattern(length)           


# Write a program that prompts the user to enter a positive integer n and prints a triangle
# pattern of numbers. The pattern should have n rows, where each row contains the numbers from 
# 1 up to the row number. Use the range function to control the number of rows and the values 
# within each row.

def triagular_pattern_of_numbers(num):
    for a in range(1, num + 1):
        for j in range(1, a + 1):
            print(j, end=" ")

        print()
num = 10
triagular_pattern_of_numbers(num)           