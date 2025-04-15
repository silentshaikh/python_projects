import random,string

def passwrodGEnerator(length,howMuch):
    lengthInt = int(length)
    howMuchInt = int(howMuch)
    totalValueForPass = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    for password in range(howMuchInt):
        passGene = ""
        for characPass in range(lengthInt):
            passGene +=  f"{random.choice(totalValueForPass)}"
    
        print(f"Generated Password : {passGene}")


lengthInp = input("Enter the amount of password , you want : ")
amountInp = input("Enter the Length of password : ")
passwrodGEnerator(lengthInp,amountInp)

