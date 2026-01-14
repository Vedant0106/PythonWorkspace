import logging
from employee_utility import (
    calculate_bonus,
    calculate_leave_deduction,
    calculate_final_salary
)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="employee_app.log",
    filemode="a"
)

logger = logging.getLogger(__name__)

WORKING_DAYS = 30

try:
    logger.info("Employee salary application started")

    employee_name = input("Enter employee name: ")
    designation = input("Enter designation (coder/designer/manager): ")

    basic_salary = float(input("Enter basic salary: "))
    if basic_salary <= 0:
        raise ValueError("Salary must be greater than zero")

    leaves_taken = int(input("Enter number of leaves taken: "))
    if leaves_taken < 0 or leaves_taken > WORKING_DAYS:
        raise ValueError("Invalid number of leaves")

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
    print("Leave Deduction   :", round(leave_deduction, 2))
    print("------------------------------------")
    print("Final Salary      :", final_salary)
    print("====================================")

    logger.info("Employee report generated successfully")

except ValueError as value_error:
    logger.error("Validation error: %s", value_error)
    print("Input Error:", value_error)

except Exception as exception:
    logger.exception("Unexpected application error")
    print("Something went wrong. Please try again.")

finally:
    logger.info("Employee salary application finished")
