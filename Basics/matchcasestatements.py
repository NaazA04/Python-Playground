x=int(input("enter number"))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _ if x==15:
        print(x)
    case _ if x==20:
        print("it is 20")

