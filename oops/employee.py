from abc import ABC, abstractmethod


# -----------------------------
# ABSTRACT BASE CLASS
# -----------------------------
class Employee(ABC):
    def __init__(self, emp_id, name, experience):
        self.emp_id = emp_id
        self.name = name
        self.experience = experience
        self.__base_salary = 0

    def set_base_salary(self, salary):
        self.__base_salary = salary

    def get_base_salary(self):
        return self.__base_salary

    @abstractmethod
    def get_bonus_percentage(self):
        pass

    def calculate_bonus(self):
        return self.get_base_salary() * self.get_bonus_percentage()

    def calculate_final_salary(self):
        return self.get_base_salary() + self.calculate_bonus()

    def show_details(self):
        print("\n-----------------------------")
        print("Employee ID   :", self.emp_id)
        print("Name          :", self.name)
        print("Experience    :", self.experience, "years")
        print("Role          :", self.__class__.__name__)
        print("Base Salary   :", self.get_base_salary())
        print("Bonus         :", round(self.calculate_bonus(), 2))
        print("Final Salary  :", round(self.calculate_final_salary(), 2))
        print("-----------------------------")


# -----------------------------
# EMPLOYEE TYPES
# -----------------------------
class Coder(Employee):
    def __init__(self, emp_id, name, experience):
        super().__init__(emp_id, name, experience)
        self.set_base_salary(60000)

    def get_bonus_percentage(self):
        return 0.10


class Designer(Employee):
    def __init__(self, emp_id, name, experience):
        super().__init__(emp_id, name, experience)
        self.set_base_salary(55000)

    def get_bonus_percentage(self):
        return 0.12


class TechLead(Employee):
    def __init__(self, emp_id, name, experience):
        super().__init__(emp_id, name, experience)
        self.set_base_salary(90000)

    def get_bonus_percentage(self):
        return 0.15


class Manager(Employee):
    def __init__(self, emp_id, name, experience):
        super().__init__(emp_id, name, experience)
        self.set_base_salary(120000)

    def get_bonus_percentage(self):
        return 0.18


class BusinessHead(Employee):
    def __init__(self, emp_id, name, experience):
        super().__init__(emp_id, name, experience)
        self.set_base_salary(200000)

    def get_bonus_percentage(self):
        return 0.25


# -----------------------------
# USER INPUT + MENU
# -----------------------------
employees = []

role_map = {
    "1": Coder,
    "2": Designer,
    "3": TechLead,
    "4": Manager,
    "5": BusinessHead
}

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Coder")
    print("2. Add Designer")
    print("3. Add Tech Lead")
    print("4. Add Manager")
    print("5. Add Business Head")
    print("6. View All Employees")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice in role_map:
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        experience = int(input("Enter experience (years): "))

        employee = role_map[choice](emp_id, name, experience)
        employees.append(employee)

        print("✅ Employee added successfully")

    elif choice == "6":
        if not employees:
            print("❌ No employees found")
        else:
            print("\n===== EMPLOYEE SALARY REPORT =====")
            for emp in employees:
                emp.show_details()

    elif choice == "7":
        print("Exiting system...")
        break

    else:
        print("❌ Invalid choice")
