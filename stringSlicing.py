# Exercise 4. String slicing and substring Removal
# Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.
#Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.
#
#Given Input:
#
#remove_chars("pynative", 4)
#remove_chars("pynative", 2)
#Expected Output:
#
#tive
#native

def remove_chars(name, index):
    remove = name[index:]

    return remove

result1 = remove_chars("pynative", 4)
result2 = remove_chars("pynative", 2)
print("\n", result1)
print("\n", result2)