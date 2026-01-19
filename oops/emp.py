# class Emp:
#     def __init__(self, name, age, emp_id, salary):
#         self.name = name
#         self.age = age
#         self.emp_id = emp_id
#         self.salary = salary

#     def show_details(self):
#         print("Name :", self.name)
#         print("Age  :", self.age)
#         print("ID   :", self.emp_id)
#         print("ID   :", self.salary)

# emp1 = Emp("Vedant", 24, 507179, 11000)

# emp1.show_details()

# class Emp:
#     def __init__(self, name, age, emp_id):
#         self.name = name
#         self.age = age
#         self.emp_id = emp_id

#     def get_details(self):
#         return {
#             "name": self.name,
#             "age": self.age,
#             "id": self.emp_id
#         }

# employees = {}

# def add_employee(emp):
#     if emp.emp_id in employees:
#         print(" Employee ID already exists", emp.emp_id, "for employee", emp.name)
#     else:
#         employees[emp.emp_id] = emp
#         print(" Employee added successfully")

# def show_all_employees():
#     if not employees:
#         print("No employees found")
#         return

#     print("\n--- EMPLOYEE LIST ---")
#     for emp_id, emp in employees.items():
#         details = emp.get_details()
#         print(
#             f"ID: {emp_id}, "
#             f"Name: {details['name']}, "
#             f"Age: {details['age']}"
#         )


# # Create employees
# emp1 = Emp("Vedant", 24, 101)
# emp2 = Emp("Rashid", 28, 102)
# emp3 = Emp("Aman", 30, 101) 
# emp4 = Emp("Manju", 35, 123) 

# # Add employees
# add_employee(emp1)
# add_employee(emp2)
# add_employee(emp3)  
# add_employee(emp4)
# # Show employees
# show_all_employees()



# #using set
# class Emp:
#     def __init__(self, name, age, emp_id):
#         self.name = name
#         self.age = age
#         self.emp_id = emp_id

#     # Define equality based on emp_id
#     def __eq__(self, other):
#         if isinstance(other, Emp):
#             return self.emp_id == other.emp_id
#         return False

#     # Hash based on emp_id (required for set)
#     def __hash__(self):
#         return hash(self.emp_id)

#     def get_details(self):
#         return {
#             "name": self.name,
#             "age": self.age,
#             "id": self.emp_id
#         }


# # SET to store employees (unique by emp_id)
# employees = set()


# def add_employee(emp):
#     if emp in employees:
#         print(
#             "Employee ID already exists",
#             emp.emp_id,
#             "for employee",
#             emp.name
#         )
#     else:
#         employees.add(emp)
#         print("Employee added successfully")


# def show_all_employees():
#     if not employees:
#         print("No employees found")
#         return

#     print("\n--- EMPLOYEE LIST ---")
#     for emp in employees:
#         details = emp.get_details()
#         print(
#             f"ID: {details['id']}, "
#             f"Name: {details['name']}, "
#             f"Age: {details['age']}"
#         )


# # Create employees
# emp1 = Emp("Vedant", 24, 101)
# emp2 = Emp("Rashid", 28, 102)
# emp3 = Emp("Aman", 30, 101)   # Duplicate ID
# emp4 = Emp("Manju", 35, 123)

# # Add employees
# add_employee(emp1)
# add_employee(emp2)
# add_employee(emp3)   # Rejected
# add_employee(emp4)

# # Show employees
# show_all_employees()

#using user input dict

# employees = {}   # emp_id -> employee details


# def get_unique_emp_id():
#     while True:
#         emp_id = input("Enter Employee ID: ").strip()

#         # Empty check
#         if not emp_id:
#             print("❌ Employee ID cannot be empty")
#             continue

#         # Numeric check
#         if not emp_id.isdigit():
#             print("❌ Employee ID must be numeric")
#             continue

#         # Unique check
#         if emp_id in employees:
#             print("❌ Employee ID already exists. Try another.")
#             continue

#         return emp_id


# def add_employee():
#     emp_id = get_unique_emp_id()

#     name = input("Enter Employee Name: ")
#     age = input("Enter Employee Age: ")
#     role = input("Enter Employee Role: ")

#     employees[emp_id] = {
#         "name": name,
#         "age": age,
#         "role": role
#     }

#     print("✅ Employee added successfully")


# def show_all_employees():
#     if not employees:
#         print("❌ No employees found")
#         return

#     print("\n------ EMPLOYEE LIST ------")
#     for emp_id, details in employees.items():
#         print(f"ID   : {emp_id}")
#         print(f"Name : {details['name']}")
#         print(f"Age  : {details['age']}")
#         print(f"Role : {details['role']}")
#         print("---------------------------")


# # -----------------------------
# # MAIN MENU
# # -----------------------------
# while True:
#     print("\n===== EMPLOYEE MANAGEMENT =====")
#     print("1. Add Employee")
#     print("2. View Employees")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_employee()
#     elif choice == "2":
#         show_all_employees()
#     elif choice == "3":
#         print("Exiting program...")
#         break
#     else:
#         print("❌ Invalid choice")

# class Employee:
#     def __init__(self, emp_id, name, age, role):
#         self.emp_id = emp_id
#         self.name = name
#         self.age = age
#         self.role = role

#     def get_details(self):
#         return {
#             "id": self.emp_id,
#             "name": self.name,
#             "age": self.age,
#             "role": self.role
#         }


# # Dictionary to store employees
# # emp_id (int) -> Employee object
# employees = {}


# def get_unique_emp_id():
#     while True:
#         emp_id = input("Enter Employee ID: ").strip()

#         if not emp_id:
#             print("❌ Employee ID cannot be empty")
#             continue

#         if not emp_id.isdigit():
#             print("❌ Employee ID must be numeric")
#             continue

#         emp_id = int(emp_id)

#         if emp_id in employees:
#             print("❌ Employee ID already exists")
#             continue

#         return emp_id


# def add_employee():
#     emp_id = get_unique_emp_id()
#     name = input("Enter Employee Name: ")
#     age = input("Enter Employee Age: ")
#     role = input("Enter Employee Role: ")

#     emp = Employee(emp_id, name, age, role)
#     employees[emp_id] = emp

#     print("✅ Employee added successfully")


# def show_all_employees():
#     if not employees:
#         print("❌ No employees found")
#         return

#     print("\n------ EMPLOYEE LIST ------")
#     for  emp in employees.items():
#         details = emp.get_details()
#         print(f"ID   : {details['id']}")
#         print(f"Name : {details['name']}")
#         print(f"Age  : {details['age']}")
#         print(f"Role : {details['role']}")
#         print("---------------------------")


# # -----------------------------
# # MAIN MENU
# # -----------------------------
# while True:
#     print("\n===== EMPLOYEE MANAGEMENT =====")
#     print("1. Add Employee")
#     print("2. View Employees")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_employee()
#     elif choice == "2":
#         show_all_employees()
#     elif choice == "3":
#         print("Exiting program...")
#         break
#     else:
#         print("❌ Invalid choice")


# ==============================
# Employee Management System
# Using OOPS (Inheritance + Polymorphism)
# ==============================


# -------- Base Class --------
class Employee:
    def __init__(self, emp_id, name, age, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def calculate_salary(self):
        # Base salary (will be overridden)
        return self.base_salary

    def get_details(self):
        return {
            "ID": self.emp_id,
            "Name": self.name,
            "Age": self.age,
            "Role": self.__class__.__name__,
            "Final Salary": self.calculate_salary()
        }


# -------- Sub Classes --------
class Manager(Employee):
    def __init__(self, emp_id, name, age, base_salary, team_size):
        super().__init__(emp_id, name, age, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        bonus = self.base_salary * 0.20
        return self.base_salary + bonus


class Developer(Employee):
    def __init__(self, emp_id, name, age, base_salary, language):
        super().__init__(emp_id, name, age, base_salary)
        self.language = language

    def calculate_salary(self):
        bonus = self.base_salary * 0.15
        return self.base_salary + bonus


class Tester(Employee):
    def __init__(self, emp_id, name, age, base_salary, tool):
        super().__init__(emp_id, name, age, base_salary)
        self.tool = tool

    def calculate_salary(self):
        bonus = self.base_salary * 0.10
        return self.base_salary + bonus


class Designer(Employee):
    def __init__(self, emp_id, name, age, base_salary, design_tool):
        super().__init__(emp_id, name, age, base_salary)
        self.design_tool = design_tool

    def calculate_salary(self):
        bonus = self.base_salary * 0.12
        return self.base_salary + bonus


# -------- Helper Function --------
def print_employee(employee):
    details = employee.get_details()
    print("\n----------------------------")
    for key, value in details.items():
        print(f"{key} : {value}")
    print("----------------------------")


# -------- Main Program --------
if __name__ == "__main__":

    # Create employee objects
    emp1 = Manager(101, "Vedant", 30, 100000, team_size=8)
    emp2 = Developer(102, "Rashid", 26, 80000, "Python")
    emp3 = Tester(103, "Aman", 28, 60000, "Selenium")
    emp4 = Designer(104, "Manju", 27, 70000, "Figma")

    # Store employees
    employees = [emp1, emp2, emp3, emp4]

    print("\n===== EMPLOYEE DETAILS =====")
    for emp in employees:
        print_employee(emp)

