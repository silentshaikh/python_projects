# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

max_length = 5
def shorter(lst:list):
    while len(lst)>max_length:
        remove_item = lst.pop()
        print(f"Remove Item : {remove_item}")
    

shorter([1,2,3,4,5,6,7,8])