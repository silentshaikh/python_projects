# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

def earth_to_mars():
    try:
        earth_weight = float(input("Enter Your Weight : "))
        #convert into mars weight
        # earth_weight * (planet_gravity / earth_gravity)
        marsWeight = earth_weight * (3.73/9.81) # 3.73m/s^2 - 9.81m/s^2
        print(f"Your Weight on Mars is {round(marsWeight,2)}kg")
    except:
        print("Please Enter ONly Number 0-9")

earth_to_mars()




# Milestone #2: Adding in All Planets

# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.

# 📊 Gravity Values of Planets (in m/s²):
# Planet	Gravity (m/s²)
# Mercury	3.7
# Venus	8.87
# Earth	9.81
# Mars	3.73
# Jupiter	24.79
# Saturn	10.44
# Uranus	8.69
# Neptune	11.15

def weight_on_more_planet(diff_planet,earth_weight,planet_gravity,earth_gravity):
    # earth_weight * (planet_gravity / earth_gravity)
        return f"Your Weight on {diff_planet} is  {round(earth_weight * (planet_gravity/earth_gravity),2)}kg"

try:

    earth_weight = float(input("Enter Your Weight : "))
    print("\nChoose an Option :\n")
    print("""
      Mercury	
      Venus	
      Earth	
      Mars	
      Jupiter	
      Saturn	
      Uranus	
      Neptune	
""")
    selectPlanet = input("Enter Your Planet : ").replace(" ",'')
    if not selectPlanet:
        print("Please Emter any Planet name")
    elif selectPlanet.lower() == "mercury":
     print(weight_on_more_planet(selectPlanet,earth_weight,3.7,9.81))
    elif selectPlanet.lower() == "venus":
        print(weight_on_more_planet(selectPlanet,earth_weight,8.87,9.81))
    elif selectPlanet.lower() == "mars":
        print(weight_on_more_planet(selectPlanet,earth_weight,3.73,9.81))
    elif selectPlanet.lower() == "jupiter":
        print(weight_on_more_planet(selectPlanet,earth_weight,24.79,9.81))
    elif selectPlanet.lower() == "saturn":
        print(weight_on_more_planet(selectPlanet,earth_weight,10.44,9.81))
    elif selectPlanet.lower() == "uranus":
        print(weight_on_more_planet(selectPlanet,earth_weight,8.69,9.81))
    elif selectPlanet.lower() == "neptune":
        print(weight_on_more_planet(selectPlanet,earth_weight,11.15,9.81))
    else:
        print("INvalid Planet")
except:
    print("Please Enter only numbers")