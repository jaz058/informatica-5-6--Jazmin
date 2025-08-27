while True:
    greeting = input("Type a greeting: ").title()
    if greeting.startswith("Hello"):
        print("$0")
    elif greeting.startswith("H"):
        print("$20")
    else:
        print("$100")
        break