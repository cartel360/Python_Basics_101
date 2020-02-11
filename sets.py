# A set is unordered collection and uindexed, doesn't allow duplicate members

names = {"Billy", "Dan"}

print(names)

#Check if a value is in a set
print("Billy" in names)

#Add to set
names.add("Okeyo")
print(names)

#Remove from set
names.remove("Dan")
print(names)

#Clearing a set
#names.clear()
#print(names)

#Let's try adding a duplicate
names.add("Billy")
print(names)