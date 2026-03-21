print("Welcome to Python Pizza Order!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill= 0
valid_order = True
size_error = False
pepperoni_error = False
extra_cheese_error = False

if valid_order:
 if size == "S":
    bill = 12
    if pepperoni == "Y":
        bill += 2
    elif pepperoni != "N":
        
        valid_order = False
        pepperoni_error = True

    if extra_cheese== "Y":
            bill += 1
    elif extra_cheese != "N": 
             
           valid_order = False  
           extra_cheese_error = True    
   

 if valid_order:
   if size == "M":
     bill = 15
     if pepperoni == "Y":
        bill += 3
     elif pepperoni != "N":
        
        valid_order = False
        pepperoni_error = True

     if extra_cheese== "Y":
        bill += 2
     elif extra_cheese != "N":
        valid_order = False
        extra_cheese_error = True


 if valid_order:
   if size == "L":
    bill = 20
    if pepperoni == "Y":
        bill += 5
    elif pepperoni != "N":
       
        valid_order = False
        pepperoni_error = True  
    if extra_cheese== "Y":
        bill += 3
    elif extra_cheese != "N":
        
        valid_order = False
        extra_cheese_error = True
  

if size not in ["S", "M", "L"]:
    
    valid_order = False
    size_error = True

if valid_order:
 print(f"your total bill will be: ${bill}") 
 print("Thank you for ordering! 🍕")


if size_error:
    print("Invalid size selection. Please choose S, M, or L.")      
if pepperoni_error:
    print("Invalid pepperoni selection. Please choose Y or N.")
if extra_cheese_error:
    print("Invalid extra cheese selection. Please choose Y or N.")


