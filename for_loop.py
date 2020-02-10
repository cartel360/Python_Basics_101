number = int(input("Enter the Number of Elements to be inserted: "))
array = []
for i in range(0, number):
    element = int(input("Enter Element: "))
    array.append(element)
average = sum(array)/number

print("Average of Elements in the list is: ", round(average,2))
