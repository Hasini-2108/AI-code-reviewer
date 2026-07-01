import math

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):

        avg=self.average()

        if avg>=90:
            return "A"

        elif avg>=75:
            return "B"

        elif avg>=60:
            return "C"

        else:
            return "D"


def factorial(n):

    if n==0:
        return 1

    result=1

    for i in range(1,n+1):
        result*=i

    return result


def prime(number):

    if number<2:
        return False

    for i in range(2,int(math.sqrt(number))+1):

        if number%i==0:
            return False

    return True


students=[

    Student("Alice",[90,95,88]),

    Student("Bob",[75,60,82]),

    Student("Charlie",[45,50,55])

]

for student in students:

    print(student.name)

    print("Average:",student.average())

    print("Grade:",student.grade())

    print()

numbers=[5,7,11,20,23]

for n in numbers:

    print("Factorial of",n,"=",factorial(n))

    print("Prime:",prime(n))

    print()

try:

    file=open("demo.txt","r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File not found")