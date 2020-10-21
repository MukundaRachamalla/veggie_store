print("**********welcome to veggie store**********")
cart = {}
def menu():
    mainmenu()
def mainmenu():
    print("vegetables:price per kg")
    avail_veg = {"carrot":50,"onion":30,"brinjal":30,"tomato":60,"":"",}
    print(avail_veg)
    choose =input("select vegetables you want to buy")
    if choose == "carrot" :
        carrot()
    elif choose == "onion":
        onion()
    elif choose == "tomato":
        tomato()
    elif choose == "brinjal":
        brinjal()
    else:
        print ("invalid choice")
        mainmenu()

def carrot():
    print("price per kg = 50/-")
    quantity = int(input("select the kg's you need: "))
    tot_price = 50 * quantity
    print("the total price of carrots is -----", tot_price)
    select = input("confirm your choice?y/n: ")
    if select == "Y" or select =="y":
        name = "carrot"
        cart[name]= tot_price
        print("successfully added to cart")
        print("do u like to shop more?Y/N")
        ca = input()
        if ca == "y" or ca == "Y":
            mainmenu()
        elif ca == "N" or ca == "n":
            cart_item()
        else:
            print("inavalid choice")
    elif select == "n" or select =="N":
        mainmenu()


def cart_item():
    print(cart)
    val = cart.values()
    tot_val = sum(val)
    print("total value of the cart", tot_val)
    print("do you want to continue shopping y/n:")
    choice_3 = input()
    if choice_3 is "Y" or choice_3 is "y":
        mainmenu()
    elif choice_3 is "N" or choice_3 is "n":
        print("thankyou for shopping / bye...")
    else:
        print("invalid input")
        cart_item()

def onion():
    print("price per kg = 30/-")
    quantity = int(input("select the kg's you need: "))
    tot_price = 30 * quantity
    print("the total price of carrots is -----", tot_price)
    select = input("confirm your choice?y/n: ")
    if select == "Y" or select =="y":
        name = "onion"
        cart[name]= tot_price
        print("successfully added to cart")
        print("do u like to shop more?Y/N")
        on = input()
        if on == "y" or on == "Y":
            mainmenu()
        elif on == "N" or on == "n":
            cart_item()
        else:
            print("inavalid choice")

    elif select  == "n" or select =="N":
        mainmenu()

def tomato():
    print("price per kg = 30/-")
    quantity = int(input("select the kg's you need: "))
    tot_price = 30 * quantity
    print("the total price of tomato is -----", tot_price)
    select = input("confirm your choice?y/n: ")
    if select == "Y" or select =="y":
        name = "tomato"
        cart[name]= tot_price
        print("successfully added to cart")
        print("do u like to shop more?Y/N")
        to = input()
        if to == "y" or to == "Y":
            mainmenu()
        elif to == "N" or to == "n":
            cart_item
        else:
            print("inavalid choice")
    elif select  == "n" or select =="N":
        mainmenu()

def brinjal():
    print("price per kg = 40/-")
    quantity = int(input("select the kg's you need: "))
    tot_price = 40 * quantity
    print("the total price of brinjal is -----", tot_price)
    select = input("confirm your choice?y/n: ")
    if select == "Y" or select =="y":
        name = "brinjal"
        cart[name]= tot_price
        print("successfully added to cart")
        print("do u like to shop more?Y/N")
        br = input()
        if br == "y" or br == "Y":
            mainmenu()
        elif br == "N" or br == "n":
            cart_item()
        else:
            print("inavalid choice")
    elif select  == "n" or select =="N":
        mainmenu()

menu()