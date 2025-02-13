print('This is another string!')

# Display the numbers 1 to 10 using a loop
for i in range (10):
    print(i+1)

# Compute the average of a set of numbers
numbers = (input("Enter a set of numbers (separated by spaces): "))
numbers = list(map(float, numbers.split()))
average = sum(numbers) / len(numbers)
print(f"The average is: {average} ")