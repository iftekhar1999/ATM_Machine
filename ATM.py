print("Welcome to City Bank !!! ")

profile = ["1234","5678","9012","3456","7890"]

for x in profile:
    n = input("Enter Your ID: ")

    if n == "1234" :
        z=0 #it can use as password if we want to make it more dynamic...
        print("Welcome Mr. Hardy")

    elif n == "5678" :
        z=1 #it can use as password if we want to make it more dynamic...
        print("Welcome Mr. Jack")

    elif n == "9012" :
        z=2 #it can use as password if we want to make it more dynamic...
        print("Welcome Mr. John")

    elif n== "3456" :
        z=3 #it can use as password if we want to make it more dynamic...
        print("Welcome Mr. Alex")

    elif n== "7890" :
        z=4 #it can use as password if we want to make it more dynamic...
        print("Welcome Mr. Henry")

    else :
        print("Wrong Input")
        continue


    my_tuple=("300000","240000","500000","340000","350000")

    def my_function(p):
        print("Total Balance : ", (my_tuple[z]))

    my_function(n)