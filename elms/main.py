from employee_utility import (
    calculate_bonus,
    calculate_leave_deduction,
    calculate_final_salary
)

WORKING_DAYS = 30

employee_name = input("Enter employee name: ")
designation = input("Enter designation (coder/designer/manager): ")
basic_salary = float(input("Enter basic salary: "))
leaves_taken = int(input("Enter number of leaves taken: "))

# Validate leaves
if leaves_taken < 0 or leaves_taken > WORKING_DAYS:
    print(f"\nError: Leaves cannot be less than 0 or more than {WORKING_DAYS} days.")
else:
    bonus = calculate_bonus(basic_salary, designation)
    salary_with_bonus = basic_salary + bonus
    leave_deduction = calculate_leave_deduction(
        salary_with_bonus,
        leaves_taken
    )
    final_salary = calculate_final_salary(
        basic_salary,
        designation,
        leaves_taken
    )

    print("\n========== EMPLOYEE REPORT ==========")
    print("Name              :", employee_name)
    print("Designation       :", designation.capitalize())
    print("Basic Salary      :", basic_salary)
    print("Bonus             :", round(bonus, 2))
    print("Salary + Bonus    :", round(salary_with_bonus, 2))
    print("Working Days      :", WORKING_DAYS)
    print("Leaves Taken      :", leaves_taken)
  #  print("Leave Deduction   :", round(leave_deduction))
    print("------------------------------------")
    print("Final Salary      :", final_salary)
    print("====================================")
