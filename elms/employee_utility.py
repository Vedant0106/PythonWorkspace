def calculate_bonus(basic_salary: float, designation: str) -> float:
    designation = designation.lower()

    if designation == "coder":
        bonus_percent = 0.10
    elif designation == "designer":
        bonus_percent = 0.15
    elif designation == "manager":
        bonus_percent = 0.05
    else:
        bonus_percent = 0.0

    return basic_salary * bonus_percent


def calculate_leave_deduction(
    salary_with_bonus: float,
    leaves_taken: int,
    working_days: int = 30,
    paid_leaves: int = 15
) -> float:
    if leaves_taken <= paid_leaves:
        return 0.0

    extra_leaves = leaves_taken - paid_leaves
    per_day_salary = salary_with_bonus / working_days

    return extra_leaves * per_day_salary


def calculate_final_salary(
    basic_salary: float,
    designation: str,
    leaves_taken: int
) -> float:
    bonus = calculate_bonus(basic_salary, designation)
    salary_with_bonus = basic_salary + bonus
    deduction = calculate_leave_deduction(salary_with_bonus, leaves_taken)

    return round(salary_with_bonus - deduction, 2)
