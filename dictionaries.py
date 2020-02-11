# A dictionary is unordered collection, changeable and indexed, it doesn't allow duplicate members

student = {
    "Name": "Billy",
    "Reg No": "BIT/001",
    "Age": 50
}

print(type(student), student)

# Get a Value from dictionaries
print(student["Name"])
print(student.get("Reg No"))

# Adding values
student["Course"] = "BIT"
print(student) 

# Getting Dictionary Keys
print(student.keys())

# Coping a Dictionary
student1 = student.copy()
student1["Year"] = "2020"
print(student1)

# Dictionary List
lecturers = [
    {"Name": "John", "Age": 50},
    {"Name": "Doe", "Age": 30}
]

print(lecturers[0])