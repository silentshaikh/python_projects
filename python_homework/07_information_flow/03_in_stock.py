# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.

BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

def num_in_stock(fruit):
    fruitsData = {
        "apple":200,
        "banana":100,
        "kiwi":200,
        "orange":300,
        "pineapple":50
    }
    if fruit in fruitsData:
        print(f'The Fruit {BOLD}{ITALIC}{fruit}{RESET} is in stock and the stock is {BOLD}{ITALIC}{fruitsData[fruit]}{RESET}.')
    else:
        print(f"This fruit is not in stock.")

fruitName = input("Enter a Fruit : ").lower().replace(" ",'')
num_in_stock(fruitName)