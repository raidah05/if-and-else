choice = int(input("Which Ride do you want bike or car : "))

if choice==1:
    print("what bike do you want?")
    print("/n 1. Scooty")
    print("/n 2. Scooter")

    choice1 = int(input("Enter your choice: "))
    if choice1 == 1:
        print("You have chosen scooty")
    else :
        print("You have chosen scooter")
elif choice==2:
    print("what car do you want?")
    print("/n 1. Sudan")
    print("/n 2. Honda")

    choice3 = int(input("Enter your choice: "))
    if choice3 == 1:
        print("You have chosen sudan")
    else :
        print("You have chosen honda")
