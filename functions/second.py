"""
Program: Student Utility Program
Purpose: Demonstrate how to define and call functions in Python
"""

def greet_student(name):
    print(f"Hello {name}, welcome to the Python class!")


def calculate_total(marks):
    return sum(marks)


def calculate_average(total, count):
    return total / count


def check_result(average):
    if average >= 40:
        return "PASS"
    return "FAIL"


def display_result(name, marks):
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = check_result(average)

    greet_student(name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


if __name__ == "__main__":
    student_name = "Upasana"
    student_marks = [65, 70, 55, 80, 60]

    display_result(student_name, student_marks)
