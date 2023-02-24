while True:
    # Get the total bill amount from the user
    while True:
        try:
            total_bill = float(input("Enter the total bill amount: $"))
            if total_bill <= 0:
                print("Error: Bill amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    # Get the tip percentage from the user
    while True:
        try:
            tip_percent = float(input("Enter the tip percentage (%): "))
            if tip_percent < 0:
                print("Error: Tip percentage cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    # Calculate the tip amount
    tip_amount = total_bill * (tip_percent / 100)

    # Calculate the total amount including tip
    total_amount = total_bill + tip_amount

    # Display the tip amount and total amount to the user
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount (including tip): ${total_amount:.2f}")

    # Ask the user if they want to calculate another tip
    again = input("Do you want to calculate another tip? (y/n) ")

    # If the user does not want to calculate another tip, break out of the loop
    if again.lower() != 'y':
        break
