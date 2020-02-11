# A list is ordered collection. It can be changed thus allows duplicate values

numbers = [1, 2, 3, 4, 5]

names = ["Billy", "Dan"]

#Get a value from list
print(numbers[2])

#Append to list
names.append("Okeyo")
print(names)

#Removing from list
numbers.remove(5)
print(numbers)

#Insert at specific position
numbers.insert(3, 10)
print(numbers)

#Remove with pop
numbers.pop(3)
print(numbers)

#reverse list
names.reverse()
print(names)

#Adding a duplicate
names.insert(2, "Dan")
print(names)