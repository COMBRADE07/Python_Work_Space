hello = "x"
print(hello)

x = -10
y = -10.20
z = 10E3
print(type(x))
print(type(y))
print(type(z))

#  random number generator

import random as r

aa = []
for i in range(0, 11):
    aa.append(r.randint(0, 50))
print(aa)

# daily used function in python
"""
    len(variable)
    list.append()
    
"""

# print pattern
# x = int(input("Enter how many lines you want"))
# for i in range(0,x):
#     print(i*"*")
#
# for i in range(x+1,0,-1):
#     print(i*"*")

# sort list
a = [1, 6, 3, 2, 5, -3, 0, 2]
print(a)
a.append(23)
print(a)
a.extend([50, 60, 10])
print(a)


#  sort using logic
def reverse_a(a):
    """
        arg: list\n
        Take input as list to sort it

    """
    t = 0
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] < a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t

    print(a)


reverse_a(a)

s = "Rhutik"
print(s)
s1 = s.encode('utf32')
print(s1)
s2 = s1.decode('utf32')
print("Decoded string is: ",s2)
