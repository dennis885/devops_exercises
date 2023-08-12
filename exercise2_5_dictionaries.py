dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

# Merge the two dictionaries into a new dictionary
merged_dict = {**dict_one, **dict_two}

# Sum up all the values in the merged dictionary
total_sum = sum(merged_dict.values())

# Print the sum of all values
print("Sum of all values:", total_sum)

# Print the maximum and minimum values of the dictionary
max_value = max(merged_dict.values())
min_value = min(merged_dict.values())

print("Maximum value:", max_value)
print("Minimum value:", min_value)
