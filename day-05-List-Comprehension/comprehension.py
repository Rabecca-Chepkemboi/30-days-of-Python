
# 1. Given a list of names, write a Python program to create a new list that contains 
# the names starting with the letter 'A' 

def names_starting_with_A(names):
    names_starting_with_A = [name for name in names if name.startswith("A")]
    return names_starting_with_A

names = ["Atenge", "Omosh", "Auko", "Vince", "Akiru"]
results = names_starting_with_A(names)
print(results)


# 2. Given a list of integers, write a Python program to create a new list that 
# contains only the positive numbers.

def get_positive_numbers(numbers):
    positive_ints = [num for num in numbers if num > 0]
    return positive_ints

numbers = [2, -5, -4, 8, 9, -3, 5, 1, 3, -7]
answer = get_positive_numbers(numbers)
print(answer)


# 3. Given a list of sentences, write a Python program to create a new list that 
# contains the words in all the sentences.

def extract_new_words(words):
    sentences = [sentence for word in words for sentence in word.split()]
    return sentences

words = ["Im an amaizing hunam being. I love ciding and hiking"]
my_result = extract_new_words(words)
print(my_result)