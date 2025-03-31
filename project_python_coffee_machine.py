print("--- Welcome to Vongsapat Coffee ---")
pricecoffee = 0
showmenu = int(input("Please Type 1 to show menu : "))
if showmenu == 1:
    print("--- Choose the menu ---")
    print("1. Espresso")
    print("2. Cappucino")
    print("3. Latte")

    menucoffee = int(input("Select coffee: "))
    if menucoffee == 1:
        print("--- Choose the type of the coffee ---")
        print("1. Hot 55 baht")
        print("2. Cold 60 baht")
        coffee1 = int(input("Select type: "))
        if coffee1 == 1:
            print("--- You chose hot Espresso 55 bath")
            pricecoffee = 55
            youMoney = int(input("Input your money: "))
            if youMoney >= pricecoffee:
                print("You recieved a change of %d bath" % (youMoney - pricecoffee))
                print("--- thank you")
            else:
                print("Not enough money")
                print("--- Please try again ---")
        elif coffee1== 2:
            print("--- You Chose Cold Espresso 60 bath")
            pricecoffee = 60
            youMoney = int(input("Input your money: "))
            if youMoney >= pricecoffee:
                print("You recieved a change of %d bath" % (youMoney - pricecoffee))
                print("--- thank you ---")
            else:
                print("Not enough money")
                print("--- Please try again ---")
        else:
            print("Sorry, something went wrong")
    elif menucoffee == 2:
        print("--- Choose the type of the coffee ---")
        print("1. Hot 55 baht")
        print("2. Cold 60 baht")
        coffee2 = int(input("Select type: "))
        if coffee2 == 1:
            print("--- You Chose Hot Cappucino 55 bath")
            pricecoffee = 55
            youMoney = int(input("Input your money: "))
            if youMoney >= pricecoffee:
                print("You recieved a change of %d bath" % (youMoney - pricecoffee))
                print("--- thank you ---")
            else:
                print("Not enough money")
                print("--- Please try again ---")
        if coffee2 == 2:
            print("--- You Chose Cold Cappucino 60 bath")
            pricecoffee = 60
            youMoney = int(input("Input your money: "))
            if youMoney >= pricecoffee:
                print("You recieved a change of %d bath" % (youMoney - pricecoffee))
                print("--- thank you ---")
            else:
                print("Not enough money")
                print("--- Please try again ---")
    elif menucoffee == 3:
        print("--- Choose the type of the coffee ---")
        print("1. Hot 55 baht")
        print("2. Cold 60 baht")
        coffee3 = int(input("Select type: "))
        if coffee3 == 1:
            print("--- You Chose Hot Latte 55 bath")
            pricecoffee = 55
            youMoney = int(input("Input your money: "))
            if youMoney >= pricecoffee:
                print("You recieved a change of %d bath" % (youMoney - pricecoffee))
                print("--- thank you ---")
            else:
                print("Not enough money")
                print("--- Please try again ---")
    else:
        print("Sorry, something went wrong")
else:
    print("Sorry, something went wrong")