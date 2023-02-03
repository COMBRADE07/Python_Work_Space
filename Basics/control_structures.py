if __name__ == '__main__':
    """
    if
    if else
    if -elif
    """
    import random as r
    x = r.randint(4,5)
    print("x: ",x)
    if x == 5:
        print("x is 5")
    else:
        print("x is not 5")

    # if - elif
    x=0
    if x == 5:
        print("x==5")
    elif x == 4:
        print("x = 4")
    else:
        print("X is unkown")




    """
    iterations,
    
    for loop:
    while loop
    
    """

    # for loop
    print("her we print hello 5 times using for loop")
    for x in range(1,6):
        print("Hello")

    print("print table of 5")
    for i in range(1,11):
        print(5*i)

    # while loop
    x=1
    print("table of 5 using while loop")
    while(x<=10):
        print(5*x)
        x+=1



    # print pattern using loops
    x = 5
    print("right angle triangle")
    for i in range(0,x,1):
        print("*"*i)

    print()
    print("inverted right angle triangle")
    for i in range(x,0,-1):
        print("*"*i)

    print("Rhutik"*3)