# ---------- SAFE INPUT FUNCTIONS ----------

def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def get_marks_input(message):
    while True:
        try:
            marks = int(input(message))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter numeric marks.")


# ---------- STUDENT CLASS ----------

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.rank = None
        self.result = None
        self.division = None
        self.calculate_result_and_division()

    def calculate_result_and_division(self):
        if self.marks < 35:
            self.result = "FAIL"
            self.division = None
        else:
            self.result = "PASS"
            if self.marks >= 75:
                self.division = "Distinction"
            elif self.marks >= 60:
                self.division = "First Division"
            elif self.marks >= 50:
                self.division = "Second Division"
            else:
                self.division = "Third Division"

    def display(self):
        print(
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Marks: {self.marks} | "
            f"Result: {self.result} | "
            f"Division: {self.division} | "
            f"Rank: {self.rank}"
        )


# ---------- TEACHER CLASS (ASSOCIATION) ----------

class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.students = []

    # ---------- CREATE ----------
    def add_student(self, student):
        if student.marks < 20:
            print("❌ Marks < 20. Student auto-deleted.")
            return

        for s in self.students:
            if s.student_id == student.student_id:
                print("❌ Student with this ID already exists.")
                return

        self.students.append(student)
        print("✅ Student added successfully.")
        self.assign_ranks()

    # ---------- READ ----------
    def display_students(self):
        if not self.students:
            print("⚠️ No students available.")
            return

        print(f"\nTeacher: {self.name} (ID: {self.teacher_id})")
        print(f"Total Strength: {self.total_strength()}")
        print("-" * 90)

        sorted_students = sorted(
            self.students,
            key=lambda s: (s.result == "FAIL", -s.marks)
        )

        for student in sorted_students:
            student.display()

    def get_student_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def search_by_name(self, name):
        found = False
        for s in self.students:
            if s.name.lower() == name.lower():
                s.display()
                found = True
        if not found:
            print("❌ Student not found.")

    # ---------- UPDATE ----------
    def update_student_marks(self, student_id, new_marks):
        student = self.get_student_by_id(student_id)

        if not student:
            print("❌ Student not found.")
            return

        if new_marks < 20:
            self.students.remove(student)
            print("❌ Marks < 20. Student auto-deleted.")
            self.assign_ranks()
            return

        student.marks = new_marks
        student.calculate_result_and_division()
        print("✅ Marks updated successfully.")
        self.assign_ranks()

    # ---------- DELETE ----------
    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if student:
            self.students.remove(student)
            print("✅ Student deleted successfully.")
            self.assign_ranks()
        else:
            print("❌ Student not found.")

    # ---------- BUSINESS LOGIC ----------
    def assign_ranks(self):
        passed = [s for s in self.students if s.result == "PASS"]
        passed.sort(key=lambda s: s.marks, reverse=True)

        for i, s in enumerate(passed, start=1):
            s.rank = i

        for s in self.students:
            if s.result == "FAIL":
                s.rank = None

    def total_strength(self):
        return len(self.students)

    def average_marks(self):
        return sum(s.marks for s in self.students) / len(self.students) if self.students else 0

    def highest_marks(self):
        return max(self.students, key=lambda s: s.marks, default=None)

    def lowest_marks(self):
        return min(self.students, key=lambda s: s.marks, default=None)


# ---------- MAIN PROGRAM ----------

teacher = Teacher(201, "Rashid")

while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Search Student by ID")
    print("6. Search Student by Name")
    print("7. Statistics")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = get_int_input("Student ID: ")
        name = input("Student Name: ")
        marks = get_marks_input("Marks: ")
        teacher.add_student(Student(sid, name, marks))

    elif choice == "2":
        teacher.display_students()

    elif choice == "3":
        sid = get_int_input("Student ID: ")
        marks = get_marks_input("New Marks: ")
        teacher.update_student_marks(sid, marks)

    elif choice == "4":
        sid = get_int_input("Student ID: ")
        teacher.delete_student(sid)

    elif choice == "5":
        sid = get_int_input("Student ID: ")
        student = teacher.get_student_by_id(sid)
        student.display() if student else print("❌ Student not found.")

    elif choice == "6":
        teacher.search_by_name(input("Student Name: "))

    elif choice == "7":
        print(f"Average Marks: {teacher.average_marks():.2f}")
        if teacher.highest_marks():
            print("\nTop Scorer:")
            teacher.highest_marks().display()
        if teacher.lowest_marks():
            print("\nLowest Scorer:")
            teacher.lowest_marks().display()

    elif choice == "8":
        print("👋 Exiting program.")
        break

    else:
        print("❌ Invalid choice.")
