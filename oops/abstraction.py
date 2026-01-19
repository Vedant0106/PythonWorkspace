from abc import ABC, abstractmethod


# -------- Abstract Parent Class --------
class Electronics(ABC):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def get_device_type(self):
        pass

    def show_basic_details(self):
        print("Brand :", self.brand)
        print("Price :", self.price)


# -------- Laptop Class --------
class Laptop(Electronics):
    def __init__(self, brand, price, ram, processor):
        super().__init__(brand, price)
        self.ram = ram
        self.processor = processor

    def power_on(self):
        print("Laptop is powering on...")

    def get_device_type(self):
        return "Laptop"

    def show_details(self):
        print("\n--- Laptop Details ---")
        self.show_basic_details()
        print("RAM       :", self.ram)
        print("Processor :", self.processor)


# -------- Mobile Class --------
class Mobile(Electronics):
    def __init__(self, brand, price, camera_mp, battery):
        super().__init__(brand, price)
        self.camera_mp = camera_mp
        self.battery = battery

    def power_on(self):
        print("Mobile is powering on...")

    def get_device_type(self):
        return "Mobile"

    def show_details(self):
        print("\n--- Mobile Details ---")
        self.show_basic_details()
        print("Camera    :", self.camera_mp, "MP")
        print("Battery   :", self.battery, "mAh")


# -------- Main Program --------
if __name__ == "__main__":
    laptop = Laptop("Dell", 70000, "16GB", "Intel i7")
    mobile = Mobile("Samsung", 35000, 64, 5000)

    # Polymorphism
    for device in (laptop, mobile):
        print("\nDevice Type:", device.get_device_type())
        device.power_on()
        device.show_details()
