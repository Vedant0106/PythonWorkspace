# ==========================
# Employee Management System
# ==========================


# -------- Parent Class --------
class Employee:
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age

    def show_basic_details(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Age         :", self.age)

    def show_details(self):
        # This will be overridden
        self.show_basic_details()


# -------- Developer Class --------
class Developer(Employee):
    def __init__(self, emp_id, name, age, language, experience):
        super().__init__(emp_id, name, age)
        self.language = language
        self.experience = experience

    def show_details(self):
        print("\n--- Developer Details ---")
        self.show_basic_details()
        print("Language    :", self.language)
        print("Experience  :", self.experience, "years")


# -------- Manager Class --------
class Manager(Employee):
    def __init__(self, emp_id, name, age, team_size, department):
        super().__init__(emp_id, name, age)
        self.team_size = team_size
        self.department = department

    def show_details(self):
        print("\n--- Manager Details ---")
        self.show_basic_details()
        print("Team Size   :", self.team_size)
        print("Department  :", self.department)


# -------- Storage --------
employees = []


# -------- Add Employee --------
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    print("\nSelect Role")
    print("1. Developer")
    print("2. Manager")

    choice = input("Enter choice: ")

    if choice == "1":
        language = input("Enter Programming Language: ")
        experience = int(input("Enter Experience (years): "))
        emp = Developer(emp_id, name, age, language, experience)

    elif choice == "2":
        team_size = int(input("Enter Team Size: "))
        department = input("Enter Department: ")
        emp = Manager(emp_id, name, age, team_size, department)

    else:
        print("❌ Invalid role selection")
        return

    employees.append(emp)
    print("✅ Employee added successfully")


# -------- View Employees --------
def view_employees():
    if not employees:
        print("❌ No employees found")
        return

    print("\n===== EMPLOYEE LIST =====")
    for emp in employees:
        emp.show_details()
        print("-------------------------")


# -------- Main Menu --------
if __name__ == "__main__":
    while True:
        print("\n===== MENU =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            add_employee()
        elif option == "2":
            view_employees()
        elif option == "3":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice")
