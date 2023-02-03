"""
    set
    s.remove('element')
    add()
    update()     : update set with new values...
    remove()
    pop()       : pop function removes element from set is unpredictable
    s1.union(s2)
    s1.intersection(s2)
    s1.difference(s2)


"""
s = {5,1, 2, 3, 1, 2, 4, 5, 6, 7}
print(s)
print(type(s))

s.add(10)
print("Adding 10 in set: ", s)

x = s.copy()
print("set s is copied into set x: ", x)

s.update([12, 50, 60])
print("Updating set with [12,50,60]: ", s)

s.pop()
s.pop()
s.pop()


print("pop function removes element from set is unpredictable: ", s)


print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("""s1 = {1,2,3,4,5,6,7,8,15}\t s2 = {0,9,8,4,2,8,6,12}\n""")
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 15}
s2 = {0, 9, 8, 4, 2, 8, 6, 12}
x = s1.union(s2)
print("s1.union(s2): ", x)

y = s1.intersection(s2)
print("s1.intersection(s2): ", y)

s.clear()
print("clear() set: ", s)




