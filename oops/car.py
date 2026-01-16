from abc import ABC, abstractmethod


# -----------------------------
# ABSTRACTION
# -----------------------------
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def calculate_price(self):
        pass

    def show_basic_details(self):
        print("Brand :", self.brand)
        print("Model :", self.model)


# -----------------------------
# INHERITANCE + ENCAPSULATION
# -----------------------------
class Car(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model)
        self.year = year
        self.__price = price   # private variable

    # Getter (Encapsulation)
    def get_price(self):
        return self.__price

    # Setter (Encapsulation)
    def set_price(self, price):
        if price > 0:
            self.__price = price

    def calculate_price(self):
        if self.year >= 2023:
            return self.__price
        return self.__price * 0.9  # depreciation

    def show_details(self):
        self.show_basic_details()
        print("Year  :", self.year)
        print("Price :", self.calculate_price())


# -----------------------------
# POLYMORPHISM + INHERITANCE
# -----------------------------
class ElectricCar(Car):
    def __init__(self, brand, model, year, price, battery_range):
        super().__init__(brand, model, year, price)
        self.battery_range = battery_range

    # Method overriding (Polymorphism)
    def calculate_price(self):
        base_price = super().calculate_price()
        subsidy = 0.1 * base_price  # government subsidy
        return base_price - subsidy

    def show_details(self):
        super().show_details()
        print("Battery Range:", self.battery_range, "km")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
print("\n--- NORMAL CAR ---")
car1 = Car("Toyota", "Fortuner", 2022, 4500000)
car1.show_details()

print("\n--- ELECTRIC CAR ---")
car2 = ElectricCar("Tesla", "Model 3", 2024, 6000000, 500)
car2.show_details()
