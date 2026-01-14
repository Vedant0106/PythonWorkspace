def check_result(marks: int) -> str:
    if marks < 50:
        return "FAIL"
    elif marks >= 90:
        return "DISTINCTION"
    elif marks >= 70:
        return "GOOD"
    else:
        return "PASS"


student_marks = int(input("Enter your marks: "))
result = check_result(student_marks)

print("Result:", result)
