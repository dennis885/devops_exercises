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

# Loop through the list of employees and print name, job, and city
print("Name, Job, City of each employee:")
for employee in employees:
    print("Name:", employee["name"])
    print("Job:", employee["job"])
    print("City:", employee["address"]["city"])
    print()

# Access the country of the second employee directly
country = employees[1]["address"]["country"]
print("Country of the second employee:", country)
