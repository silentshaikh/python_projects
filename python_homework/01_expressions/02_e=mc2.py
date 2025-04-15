# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!

def equivalentEnergy():
    try:

        massofKg = float(input("Enter the mass in kg : "))
        c = 299792458
        energyOfJoules = massofKg * c**2
        print("### Joules of Energy ###")
        print(f"{energyOfJoules}  joules of energy!")
    except:
        print("Please Enter Only Number")

equivalentEnergy()
