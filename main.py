while True:
    # Get the total bill amount from the user
    total_bill = float(input("Enter the total bill amount: $"))

    # Get the tip percentage from the user
    tip_percent = float(input("Enter the tip percentage (%): "))

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
