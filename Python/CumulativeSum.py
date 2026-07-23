print("Printing current and previous number sum in a range of range(10)")
# Previous number
pre_number = 0

for number in range(10):
    sum_of_numbers = number + pre_number # keep on adding each number with the previous one
    print(f"Current Number {number} Previous Number {pre_number} Sum: {sum_of_numbers}")
    pre_number = number # Update previous_num for the next iteration