while True:

    print("\n CALCULATOR ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator Closed")
        break

    if choice == "1":
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Answer =", a + b)

    elif choice == "2":
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Answer =", a - b)

    elif choice == "3":
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Answer =", a * b)

    elif choice == "4":
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        if b == 0:
            print("Cannot Divide By Zero")
        else:
            print("Answer =", a / b)

    else:
        print("Invalid Choice")