class Student:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.reportcard = subject
        self.grade = ''

    def add_subject(self, subject, marks):
        self.reportcard[subject] = marks

    def calculate_average(self):
        total = 0
        for subject, marks in self.reportcard.items():
            total += marks
        return total / len(self.reportcard) if self.reportcard else 0

    def assign_grade(self):
        avg = self.calculate_average()
        if avg >= 80:
            self.grade = 'A'
            print("Grade A")
        elif avg >= 60:
            self.grade = 'B'
            print("Grade B")
        elif avg >= 40:
            self.grade = 'C'
            print("Grade C")
        else:
            self.grade = 'F'
            print("Grade F")

    apply_bonus = lambda self: self.calculate_average() + 5

    def generate_report(self):
        self.assign_grade()
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        print("Report Card:")
        for subject, marks in self.reportcard.items():
            print(f"{subject}: {marks}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Grade: {self.grade}\n")
            file.write("Report Card:\n")
            for subject, marks in self.reportcard.items():
                file.write(f"{subject}: {marks}\n")

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            name = lines[0].strip().split(": ")[1]
            age = int(lines[1].strip().split(": ")[1])
            grade = lines[2].strip().split(": ")[1]
            reportcard = {}
            for line in lines[4:]:
                subject, marks = line.strip().split(": ")
                reportcard[subject] = int(marks)
            studentnew = Student(name, age, reportcard)
            studentnew.generate_report()

print("Creating a new student...")
student = Student("Uzair", 21, {})
student.add_subject("Math", 85)
student.add_subject("Science", 90)

while True:
    print("\nChoose an option:")
    print("1. Generate Report")
    print("2. Apply Bonus")
    print("3. Save to File")
    print("4. Load from File")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            student.generate_report()
        case 2:
            bonus_avg = student.apply_bonus()
            print(f"Average after bonus: {bonus_avg}")
        case 3:
            student.save_to_file("report.txt")
            print("Saved to file.")
        case 4:
            Student.load_from_file("report.txt")
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice.")
            break
