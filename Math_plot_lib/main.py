# if __name__ == '__main__':
#     x = memoryview(b"Hello")
#     print(x)
#     print(x[0])
#     print(x[1])
# v = "Rhutik"
# m = hash(v)
# print(m)
#




N = int(input("Enter size: "))
# s = input("Enter String: ")
S = input("Enter String: ").lower()
#list for store vowels
V = ['a', 'e', 'i', 'o', 'u']
#initilize list to zero
X = [0]*N
#counters
cnt = 0
cnt_g = 0
k=0
#logic
for i in S:
    if i in V:
        X[k]=1
        if(X[k-1]==1):
            cnt += 1
        else:
            cnt=0
            for j in S:
                if j in V:
                    cnt_g+=1
    k += 1
if cnt ==0 and cnt_g>=1:
    print(1)
else:
    print(cnt)
print(X)



