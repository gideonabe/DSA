# class variables - Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

  class_year = 2025
  num_students = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrict", 35)
print(f"Number of graduating students of {Student.class_year} is {Student.num_students}")