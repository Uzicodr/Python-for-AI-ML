def avg(marks):
    total = 0
    for key in marks:
        total += marks[key]

    average = total / len(marks)
    return average

upgrading = lambda grade: grade+5

name=input("Enter you name: ")
age=input("Enter your age: ")

marks = {"Phy":0 , "Chem":0 , "Math":0 }

for key in marks:
    marks[key] = int(input(f"Enter your marks in {key}: "))

grade=avg(marks)

if(grade>=80):
    print(f"Congratulations {name}! You have scored {grade} marks and your grade is A")
    char='A'
elif(grade>=60):
    print(f"Congratulations {name}! You have scored {grade} marks and your grade is B")
    char='B'
elif(grade>=40):
    print(f"Congratulations {name}! You have scored {grade} marks and your grade is C")
    char='C'
else:
    print(f"Sorry {name}! You have scored {grade} marks and your grade is F. Better luck next time!")
    char='F'

choice=input("Give 5 bonus marks? (yes/no): ")
if choice.lower=="yes":
    upgrading(grade)
    print(f"Your new grade is {grade} after bonus marks.")
else:  
    print(f"Your grade remains {grade}.")

with open("file.txt", "w") as file:
    file.write(f"Name: {name}\nAge: {age}\n")
    for key in marks:
        file.write(f"{key}\t {marks[key]}\n")
    file.write(f"Average Marks: {grade}\n")
    file.write(f"Grade: {char}\n")