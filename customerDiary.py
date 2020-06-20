def customerDetails(fName, lName, address, mobile) :
    print("Following are your details: ")
    print("First Name: " , fName)
    print("Last Name: " , lName)
    print("Address: " , address)
    print("Mobile: " , mobile)
    print("Type \"Y\" for correct and \"N\" for incorrect" )
    check = input()
    if check == "Y":
        print("Thanks")
    elif check == "N" :
        print("Sorry")
        takeDetails()

def greetings():
    print("Welcome to the Chi-Store !")
    print("Please enter your details : ")

def takeDetails():
    print("First Name: ", end="")
    fName = input()
    print("Last Name: ", end="")
    lName = input()
    print("Address: ", end="")
    address = input()
    print("mobile: ", end="")
    mobile = input()
    customerDetails(fName,lName,address,mobile)

greetings()
takeDetails()
