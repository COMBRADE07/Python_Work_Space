"""
    list functions:
        l.append(value)
        l.extend(value/list)
        l.remove(value)
        l.pop(index)
        l.count("value")
        l.index(e)
        l.insert(i,e)
        l.sort()
        l.reverse() : if reverse =Ture then it will reverse the list
"""

l = [1, 8, 3, 2, 6, 0, 2, 1, 5, 7, 3, 99, 5, 2, 67, 30, -12]

print("original list is: ", l)
print("List contains 2:", l.count(2), " times")
print("l.append: 3")
l.append(3)
print(l)
l.insert(0, 25)
print("25 inserted at 0th index: ", l)
l.pop(0)
print("pop() removed 0th index from list: ", l)
l.remove(8)
print("remove() removed 8 from list: ", l)
l.extend([10, 20, 30])
print("list extended by [10, 20, 30]: ", l)
l2 = l.copy()
print("l2 is copy of l1: ", l2)
l.sort()
print("list is sorted by sort(): ", l)
l.sort(reverse=True)
print("list is sorted by sort() reverse=true: ", l)

l.reverse()
print("list is reversed: ", l)
