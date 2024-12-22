def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with a potential error:
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [10,20,30,40,50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

#More robust solution
def calculate_average_robust(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers) 