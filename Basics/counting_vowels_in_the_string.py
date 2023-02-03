# counting the vowels in given string
vowels = "aeiou"
s1 = "my name is chaudhari Rhutik"
cnt = 0
for i in vowels:
    cnt += s1.count(i)
print("vowels in s1 is: ", cnt)