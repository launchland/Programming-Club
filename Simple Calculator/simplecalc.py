# Simple Calculator Assignment
# Submitted by launchland
# Challenge by SaladStik

#intro
print("""
Welcome to the           8                        8        
                         8                        8        
.oPYo. o8 ooYoYo. .oPYo. 8 .oPYo.   .oPYo. .oPYo. 8 .oPYo. 
Yb..    8 8' 8  8 8    8 8 8oooo8   8    ' .oooo8 8 8    ' 
  'Yb.  8 8  8  8 8    8 8 8.       8    . 8    8 8 8    . 
`YooP'  8 8  8  8 8YooP' 8 `Yooo'   `YooP' `YooP8 8 `YooP' 
:.....::....:..:..8 ....:..:.....::::.....::.....:..:.....:
::::::::::::::::::8 :::::::::::::::::::::::::::::::::::::::
::::::::::::::::::..:::::: AKA calc is short for calculator""")

#used for
running = True

while running == True:
    #input for numbers
    num1 = float(input("\nEnter your first number: "))
    num2 = float(input("Enter your second number: "))

    #input for operation
    print("""\nOPERATIONS:
    •    Addition (+)
    •    Subtraction (-)
    •    Multiplication (*)
    •    Division (/)""")
    op = input("Choose an operation (+, -, *, /): ")

    #performs operation with number inputs
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid input!")
        continue
    print(f"Your answer to {num1} {op} {num2} is: {result}")

    #asks user to end loop or not
    running = input("\nWould you like to perform another operation? (Y, N): ").upper()
    if running == "Y":
        running = True
    else:
        #running != True, ends program
        print("\nThank you for using Simple Calc! Goodbye!")

