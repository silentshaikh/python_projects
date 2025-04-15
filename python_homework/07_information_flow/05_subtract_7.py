# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):
    return f"The Result of Subtraction is {num-7}"

def main():
    ourNum = 7
    subtractResult = subtract_seven(ourNum)
    print(subtractResult)

main()