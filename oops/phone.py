class Phone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def show_details(self):
        print("Brand   :", self.brand)
        print("Model   :", self.model)
        print("Price   :", self.price)
        print("Storage :", self.storage)


# Create objects
p1 = Phone("Samsung", "S23", 70000, "256GB")
p2 = Phone("Apple", "iPhone 14", 80000, "128GB")

# Display details
p1.show_details()
print()
p2.show_details()
