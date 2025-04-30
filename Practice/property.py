class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    @property
    def average(self):
        return (self.mark1+self.mark2+self.mark3)/3
    
stud1 = Student("Aditya", 10, 20, 30)
print(stud1.average)
stud1.mark1 = 50
print(stud1.average)

stud2 = Student("Lipsa", 40, 50, 60)
print(stud2.average)