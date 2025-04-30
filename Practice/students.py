#Create a student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def Average(self):
        print("Average: ",(self.mark1+self.mark2+self.mark3)/3)

    @staticmethod #decorator 
    def sayGhusuri():
        print("Bhagyashree is a Ghusuri")

stud1 = Student("Aditya", 10, 20, 30)
stud2 = Student("Lipsa", 40, 50, 60)
stud3 = Student("Bhagyashree", 70, 80, 90)

stud1.Average()
stud2.Average()
stud3.Average()

Student.sayGhusuri()
stud1.sayGhusuri()