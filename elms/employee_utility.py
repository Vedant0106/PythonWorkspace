import logging

logger = logging.getLogger(__name__)


def calculate_bonus(basic_salary: float, designation: str) -> float:
    logger.info("Calculating bonus for designation: %s", designation)

    designation = designation.lower()

    if designation == "coder":
        bonus_percent = 0.10
    elif designation == "designer":
        bonus_percent = 0.15
    elif designation == "manager":
        bonus_percent = 0.05
    else:
        logger.warning("Unknown designation entered: %s", designation)
        bonus_percent = 0.0

    bonus = basic_salary * bonus_percent
    logger.info("Bonus calculated: %.2f", bonus)
    return bonus


def calculate_leave_deduction(
    salary_with_bonus: float,
    leaves_taken: int,
    working_days: int = 30,
    paid_leaves: int = 15
) -> float:
    logger.info("Calculating leave deduction")

    if leaves_taken <= paid_leaves:
        logger.info("Leaves within paid limit, no deduction")
        return 0.0

    extra_leaves = leaves_taken - paid_leaves
    per_day_salary = salary_with_bonus / working_days
    deduction = extra_leaves * per_day_salary

    logger.info(
        "Leave deduction calculated: %.2f for %d extra leaves",
        deduction,
        extra_leaves
    )
    return deduction


def calculate_final_salary(
    basic_salary: float,
    designation: str,
    leaves_taken: int
) -> float:
    logger.info("Starting final salary calculation")

    bonus = calculate_bonus(basic_salary, designation)
    salary_with_bonus = basic_salary + bonus
    deduction = calculate_leave_deduction(salary_with_bonus, leaves_taken)

    final_salary = salary_with_bonus - deduction
    logger.info("Final salary calculated: %.2f", final_salary)

    return round(final_salary, 2)
