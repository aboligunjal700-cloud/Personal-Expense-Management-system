total=0
limit=float(input("Enter your spending limit:"))
while True:
    print("\n===EXPENSE TRACKER===")
    print("1.Add Expense")
    print("2.View Total Expense with Dates")
    print("3.Exit")

    num=input("Enter your num:")

    if num=="1":
        date=input("Enter date(DD/MM/YY):")
        category=input("Enter category(Food,Travel,Shopping,etc.):")
        amount=float(input("Enter amount spent : "))

        total += amount 
        remaining=(limit - total)
        print("\nExpense Added!")
        print(f"Date:{date}")
        print(f"Category:{category}")
        print(f"Amount:₹{amount}")

        if total>limit:
            print("Warning : You have crossed your spending limit")

    elif num=="2":
        print(f"Total Expense:₹{total}")
        print(f"Spending Limit: ₹{limit}")


        if total > limit:
            print("You have exceeded your limit")
            print("Be Carefull")
        else:
            print("You are within your limit.")
            print(f"you still have :₹{remaining}")
    elif num=="3":
        print("Goodbye!")
        break 

    else:
        print("Invalid num!please try again.")
print("Have a nice day")