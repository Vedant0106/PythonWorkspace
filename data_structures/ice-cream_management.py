# ===============================
# SCOOPS & SCRIPTS ICE CREAM SYSTEM
# ===============================

# Fixed data (immutable)
SIGNATURE_FLAVORS = ("Vanilla", "Chocolate", "Strawberry")

FLAVOR_PRICES = {
    "Vanilla": 40,
    "Chocolate": 50,
    "Strawberry": 45
}

SERVING_TYPES = frozenset({"Cone", "Cup"})

GST_RATE = 0.05  # 5% GST

cart = []
order_history = []


def show_menu():
    print("\n🍦 ICE CREAM MENU 🍦")
    for flavor in SIGNATURE_FLAVORS:
        print(f"{flavor} - ₹{FLAVOR_PRICES[flavor]}")
    print("----------------------")


def add_to_cart():
    flavor = input("Enter flavor: ").capitalize()
    if flavor not in SIGNATURE_FLAVORS:
        print("❌ Invalid flavor")
        return

    serving = input("Enter serving type (Cone/Cup): ").capitalize()
    if serving not in SERVING_TYPES:
        print("❌ Invalid serving type")
        return

    toppings_input = input("Enter toppings (comma separated, optional): ")
    toppings = set()

    if toppings_input.strip():
        toppings = {t.strip().lower() for t in toppings_input.split(",")}

    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("❌ Quantity must be positive")
        return

    item_price = FLAVOR_PRICES[flavor]

    cart_item = {
        "flavor": flavor,
        "serving": serving,
        "toppings": toppings,
        "quantity": quantity,
        "price": item_price
    }

    cart.append(cart_item)
    print("✅ Item added to cart")


def calculate_discount(subtotal):
    if subtotal >= 300:
        return subtotal * 0.10
    if subtotal >= 200:
        return subtotal * 0.05
    return 0.0


def generate_bill():
    if not cart:
        print("🛒 Cart is empty")
        return

    print("\n========== BILL ==========")
    subtotal = 0

    for item in cart:
        item_total = item["price"] * item["quantity"]
        subtotal += item_total
        print(
            f'{item["flavor"]} ({item["serving"]}) x {item["quantity"]} '
            f'= ₹{item_total}'
        )

    discount = calculate_discount(subtotal)
    gst = (subtotal - discount) * GST_RATE
    final_amount = subtotal - discount + gst

    print("--------------------------")
    print("Subtotal       : ₹", round(subtotal, 2))
    print("Discount       : ₹", round(discount, 2))
    print("GST (5%)       : ₹", round(gst, 2))
    print("Final Amount   : ₹", round(final_amount, 2))
    print("==========================")

    order_history.append({
        "items": cart.copy(),
        "total": final_amount
    })

    cart.clear()


def show_order_history():
    if not order_history:
        print("📭 No previous orders")
        return

    print("\n📜 ORDER HISTORY")
    for index, order in enumerate(order_history, start=1):
        print(f"\nOrder {index} - Total ₹{round(order['total'], 2)}")


# ===============================
# MAIN PROGRAM LOOP
# ===============================
while True:
    print("\n1. Show Menu")
    print("2. Add to Cart")
    print("3. Generate Bill")
    print("4. Order History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        generate_bill()
    elif choice == "4":
        show_order_history()
    elif choice == "5":
        print("\n🍨 Thank you for visiting Scoops & Scripts!")
        break
    else:
        print("❌ Invalid choice")
