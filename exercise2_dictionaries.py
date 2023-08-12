employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Update the job to "Software Engineer"
employee["job"] = "Software Engineer"

# Remove the "age" key from the dictionary
del employee["age"]

# Loop through the dictionary and print key:value pairs
for key, value in employee.items():
    print(key + ":", value)
