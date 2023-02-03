# build-in functions
"""
    input()
    eval():         used for string evaluation
    type()          return types of variable
    round()
    type_casting
"""
# user defined functions
"""
    def function_name(arguments):
        functions definition
        
"""
if __name__ == '__main__':
    # 1 input()
    #a = input("Enter number")

    # 2 eval(): it operates on string
    x = eval('5+5')
    print(x)
     # we can merge above two functions
    # y = eval(input("Enter the expression: "))
    # print(y)

    # 3 type()
    print(type(x))

    # 4 round()
    print(round(30.65555))
    print(round(6.356))


    # type casting
    a= 'This is rhutik'
    print(type(a))

    # string to float
    a = float('6.33')
    print(type(a))

    # string to int
    # a = '2'
    # int(a)

    # float to string      : str keyword are used
    # a = 3.2
    # str(a)
    # print(type(a))

    import random as r
    x = r.randint(0,5)
    print(x)

    # importing user defined function from different files
    # in this example we have imported main function file  and used sqr function in it.
    import main as m
    print(m.sqr(10))



