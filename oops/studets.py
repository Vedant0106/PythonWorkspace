class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_result(self):
        if self.marks >= 90:
            return "DISTINCTION"
        elif self.marks >= 70:
            return "GOOD"
        elif self.marks >= 50:
            return "PASS"
        else:
            return "FAIL"

    def display_student_details(self):
        print("\n------ STUDENT REPORT ------")
        print("Name       :", self.name)
        print("Roll No    :", self.roll_no)
        print("Marks      :", self.marks)
        print("Result     :", self.calculate_result())
        print("----------------------------")


# Main Program
students = []

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("❌ Marks must be between 0 and 100")
            continue

        student = Student(name, roll_no, marks)
        students.append(student)
        print("✅ Student added successfully")

    elif choice == "2":
        if not students:
            print("No student records found")
        else:
            for student in students:
                student.display_student_details()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("❌ Invalid choice")
