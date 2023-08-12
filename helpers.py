def find_youngest_employee(employees):
    youngest_employee = min(employees, key=lambda emp: emp["age"])
    print("Youngest employee:")
    print("Name:", youngest_employee["name"])
    print("Age:", youngest_employee["age"])

def count_upper_lower_case(string):
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    print("Uppercase letters count:", uppercase_count)
    print("Lowercase letters count:", lowercase_count)

def print_even_numbers(numbers):
    print("Even numbers:")
    for num in numbers:
        if num % 2 == 0:
            print(num)
