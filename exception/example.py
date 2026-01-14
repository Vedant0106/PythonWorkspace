marks = float(input("Enter student marks: "))

if marks < 0 or marks > 100:
    raise ValueError("Marks must be between 0 and 100")

if marks >= 99:
    print("PASS 👏👏")
    print("You're the topper of the country! 🇮🇳")
elif marks >= 95:
    print("PASS 👏👏")
    print("Awesome job! 🌟")
elif marks >= 90:
    print("PASS 👏")
    print("Great performance!")
elif marks >= 50:
    print("PASS")
else:
    print("FAIL")
