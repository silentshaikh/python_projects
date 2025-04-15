# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def feetToInches():
    try:

        inputforFeet = float(input("Enter your feet to convert into inches : "))
        print("\n ### FEET TO INCHES ### \n")
        print(f"{inputforFeet} Feet is equal to {inputforFeet*12} Inches.")
    except:
        print("Please Enter a Number")

feetToInches()