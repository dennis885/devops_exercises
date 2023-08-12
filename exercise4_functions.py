from helpers import find_youngest_employee, count_upper_lower_case, print_even_numbers

# Example usage of the functions
employees = [
    {
        "name": "Tina",
        "age": 30,
        "birthday": "1990-03-10",
        "job": "DevOps Engineer",
        "address": {
            "city": "New York",
            "country": "USA"
        }
    },
    {
        "name": "Tim",
        "age": 35,
        "birthday": "1985-02-21",
        "job": "Developer",
        "address": {
            "city": "Sydney",
            "country": "Australia"
        }
    }
]

find_youngest_employee(employees)

input_string = "Hello World"
count_upper_lower_case(input_string)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(numbers)
