# 1. Check Anagram: Write a function that takes two strings as input and returns True if the strings
# are anagrams (contain the same characters in a different order), and False otherwise.

def checkAnagram(a, b):
    if(sorted(a) == sorted(b)):
        print("They are anagram")
    else:
        print("They are not anagram")   
checkAnagram("African", "Africana")         
 

# 2. Longest Common Prefix: Write a function that takes an array of strings as input and returns the 
# longest common prefix among all the strings. 

names = ["Clarah", "Issabella", "Vince"]
longest_name = max(names, key=len)
print(longest_name)


# 3. Count Substrings: Write a function that takes a string and a substring as input and returns the 
# count of occurrences of the substring in the string.

count_occurences= "nice, this place is nice, nice"
occurence = "nice"
occur = count_occurences.count(occurence)
print(occur)


# 5. Remove Whitespace: Write a function that takes a string as input and returns the string with all
# whitespace characters removed.

def removeWhiteSpace(str):
    return str.replace(" ", "")

str = "c l a r a h"
print(removeWhiteSpace(str))