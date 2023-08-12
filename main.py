my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]

# Print elements higher than or equal to 10
print("Elements higher than or equal to 10:")
for num in my_list:
    if num >= 10:
        print(num)

# Create a new list with elements higher than or equal to 10
new_list = [num for num in my_list if num >= 10]
print("New list with elements higher than or equal to 10:", new_list)

# Ask user for a number and print elements higher than the user's input
user_input = int(input("Enter a number: "))
filtered_list = [num for num in my_list if num > user_input]
print("Filtered list with elements higher than", user_input, ":", filtered_list)
