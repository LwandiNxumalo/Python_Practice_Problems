word = "pynative"

print(f"Original String is {word}")
print("Printing only even index chars")

for char in range(0, len(word) - 1, 2):
    print(word[char])