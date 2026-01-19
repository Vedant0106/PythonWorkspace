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

class Emp:
    def __init__(self, name, age, emp_id):
        self.name = name
        self.age = age
        self.emp_id = emp_id

    def get_details(self):
        return {
            "name": self.name,
            "age": self.age,
            "id": self.emp_id
        }

employees = {}

def add_employee(emp):
    if emp.emp_id in employees:
        print(" Employee ID already exists")
    else:
        employees[emp.emp_id] = emp
        print(" Employee added successfully")

def show_all_employees():
    if not employees:
        print("No employees found")
        return

    print("\n--- EMPLOYEE LIST ---")
    for emp_id, emp in employees.items():
        details = emp.get_details()
        print(
            f"ID: {emp_id}, "
            f"Name: {details['name']}, "
            f"Age: {details['age']}"
        )


# Create employees
emp1 = Emp("Vedant", 24, 101)
emp2 = Emp("Rashid", 28, 102)
emp3 = Emp("Aman", 30, 101)  

# Add employees
add_employee(emp1)
add_employee(emp2)
add_employee(emp3)  

# Show employees
show_all_employees()

