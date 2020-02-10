class students():
    def __init__(self, name, reg, age, school, dept):
        self.name = name
        self.reg = reg
        self.age = age
        self.school = school
        self.dept = dept

student1 = students("Billy", "BIT/54373/2016", 50, "Computing & Informatics", "Information Technology")

student1.campus = "Thika"


#print("Student Name: " + student1.name + "\nStudent Reg No: " + student1.reg + "\nAge: ", student1.age,
      #"\nSchool: " + student1.school + "\nDepartment: " + student1.dept)
#print(student1.__dict__)

class lecturers(students):
    pass

lecturer1 = lecturers("John" , 1, 50, "Computing & Informatics", "Information Technology")
print(lecturer1.__dict__)
        
