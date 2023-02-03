"""
    String /////
    - its a sequence of characters enclosed within the quotes.
    - string is immutable.
    - len()     calculate the string length
    - slicing : retrieving the substring
    - for example abc[start : end-1]

    = build-in functions:
    - count('char'):    count the character in given string
    - find(arg) & rfind(arg)  finding the 1st occurrence of given string as argument
    - functions: capitalize()
                 upper()
                 lower()
                 title()
                 swapcase()
                 isupper()
                 islower()
                 istitle()
                 ----This trip() are used to remove white space from string
                 strip()    remove all white space
                 ltrip()    remove white space from left
                 rtrip()    remove white space from right

                 replace()      e.g s.replace(str1,str2)    :: here str1 get replaced by str2 in s string
                 split()        e.g. s.split(',')
                 partition()    e.g. s.partition(',')
                 encode()       for example 'hello'.encode('utf8')
                 decode()       similar above

                 join()         join two string
                 isalpha()
                 isdigit()
                 isnum()
                 s.startswith(str1)
                 s.endswith(str1)




"""
import re

if __name__ == '__main__':
    s = "This is Rhutik"

    # len() and type()
    print(type(s))
    print(len(s))

    # slicing [ start : stop : step ]
    print(s[:])  # print all string
    print(s[5:8])  # print string between index 5-8

    # count()

    x = 'abcdc'
    print("c in x is:", x.count('c'), "times.")

    # counting the vowels in given string
    vowels = "aeiou"
    s1 = "my name is chaudhari Rhutik"
    cnt = 0
    for i in vowels:
        cnt += s1.count(i)
    print("vowels in s1 is: ", cnt)

    # 3 find() and rfind()
    color = 'red,green,blue,orange,yellow,purple,red,indigo,black'
    print("position of red color from start: ", color.find('red'))
    print("position of red color from end: ", color.rfind('red'))

    # 4 capitalize(), upper(), lower(), title(), swapcase()
    s = 'rhutik'
    s1 = 'RHUTIK'
    s3 = 'rUtIk'
    print("functions o/p for writing content: ", s.capitalize(), s.upper(), s1.lower(), s3.title(), s3.swapcase())

    # 5 reverse the string
    sm = "abc"
    sm2 = sm[::-1]  # list comprehension + negative indexing
    print(sm2)

    # 6 encoding and decoding
    str1 = "Hey, Rhutik."
    s = str1.encode('utf32')
    print(s)
    s = s.decode('utf32')
    print(s)

    # 7 patter matching
    strc = "welcome to pycharm"
    m = re.search("to", strc)
    print(m.group())
