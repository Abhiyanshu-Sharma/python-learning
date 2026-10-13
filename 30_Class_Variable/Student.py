class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student2 = Student("Squidward", 55)
student2 = Student("Sandy", 27)

print(student2.name)
print(student2.age)
print(f"My graduating class of {Student.class_year} has {Student.num_students}")