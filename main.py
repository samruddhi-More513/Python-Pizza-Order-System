while True:

    print("Welcome to Python Pizza Order!")

    size = input("What size pizza do you want? S, M or L: ").upper()
    if size not in ["S", "M", "L"]:
        print("Invalid size selection. Please choose S, M, or L.")
        continue

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    if pepperoni not in ["Y", "N"]:
        print("Invalid pepperoni selection. Please choose Y or N.")
        continue

    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
    if extra_cheese not in ["Y", "N"]:
        print("Invalid extra cheese selection. Please choose Y or N.")
        continue


    bill= 0
    valid_order = True

    if valid_order:
     if size == "S":
        bill = 12
        if pepperoni == "Y":
            bill += 2
        if extra_cheese== "Y":
            bill += 1
       

     if valid_order:
       if size == "M":
         bill = 15
         if pepperoni == "Y":
            bill += 3
         if extra_cheese== "Y":
            bill += 2


     if valid_order:
       if size == "L":
        bill = 20
        if pepperoni == "Y":
            bill += 5
        if extra_cheese== "Y":
            bill += 3
      

    if valid_order:
     print(f"your total bill will be: ${bill}") 
     print("Thank you for ordering! 🍕")

    # 🔁 REORDER OPTION
    again = input("\nDo you want to order again? (Y/N): ").upper()
    if again != "Y":
        print("Goodbye! 👋")
        break

