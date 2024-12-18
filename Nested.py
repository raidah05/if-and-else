medical = input("Did you have any medical cause - Y or N : ")
attend = int(input("Attendence : "))

if medical == "Y" or medical == "y":
    print("You are allowed")
else:
    if attend >= 75 :
        print("You are allowed")
    else:
        print("You are not allowed")
