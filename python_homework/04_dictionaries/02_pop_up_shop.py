# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5

fruit_data = {"apple":1,"durain":3,"jackfruit":2,"kiwi":1,"rambuton":1,"mango":2}
total_price = 0
def buy_fruits():
    global total_price 
    for key,value in fruit_data.items():
        fruitPrice = input(f"Enter how much {key} - {value}$, You want to buy")
        print("If you don't want to buy that apple so simply type 0")
        if not fruitPrice:
            print("Please Enter the price if you don't")
        else:    
            fruitPrice = int(fruitPrice)
            priceOfEachFruit = value *fruitPrice
            total_price += priceOfEachFruit
    print(f"\n Total Price : {total_price}$ \n")

buy_fruits()
