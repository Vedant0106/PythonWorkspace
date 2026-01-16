class Person:
    def __init__(self, name, age):
        # Public
        self.name = name

        # Protected
        self._city = "Bangalore"

        # Private
        self.__salary = 50000

    def show_inside_class(self):
        print("\n--- Inside Class ---")
        print("Public name      :", self.name)
        print("Protected city   :", self._city)
        print("Private salary   :", self.__salary)


class Employee(Person):
    def show_inside_child(self):
        print("\n--- Inside Child Class ---")
        print("Public name      :", self.name)
        print("Protected city   :", self._city)
        # print(self.__salary)  ❌ Not accessible
        print("Private salary   : Not accessible directly")
        

# Create object
p = Person("Vedant", 24)

# Access inside class
p.show_inside_class()

print("\n--- Outside Class ---")

# Public access
print("Public name      :", p.name)

# Protected access (allowed but discouraged)
print("Protected city   :", p._city)

# Private access (will cause error if uncommented)
# print(p.__salary)

print("Private salary   : Not accessible")

# Access private using name mangling (for demonstration)
print("Private salary (via mangling):", p._Person__salary)

# Access from child class
e = Employee("Amit", 28)
e.show_inside_child()
