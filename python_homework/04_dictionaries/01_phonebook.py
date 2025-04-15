# In this program we show an example of using dictionaries to keep track of information in a phonebook.
def create_phone_num_obj():
    phoneBook = {}
    while True:
        userName = input("ENter Your Name : ")
        userNum = input("Enter Your Number")
        if not userName or not userNum:
            print("Please Enter Your Name & Number")
        elif not userNum.isdigit():
            print("Please Enter only Number (0-9) in number input")
        else:
            phoneBook[userName.lower()] = userNum
        addMore = input("Do you want to add more (yes | no) :")
        if addMore.lower() == "yes":
            continue
        else:
            break
    return phoneBook

phone_book = create_phone_num_obj() 
print(phone_book)

def print_phone_book(phoneBook:dict):
    print("\n ### USER PHONE BOOK ### \n")
    for key,value in phoneBook.items():
        print(f"{key} : {value}")

print_phone_book(phone_book)

def lookup_user_number(phoneBook:dict):
    print("\n ### LOOK UP USERS WITH THEIR NAMES ### \n")
    while True:
        userName = input("Enter Your Name : ").lower()
        if not userName:
            print("\n Please Enter Your Name & Number \n")
        elif  userName not in phone_book :
            print(f" \n {userName} is not available \n")
        else:
            print(f"\n {userName} : {phoneBook[userName]} \n")
        addMore = input("Do you want to add more (yes | no) :")
        if addMore.lower() == "yes":
            continue
        else:
            break

lookup_user_number(phone_book)
