'''li = [2,3,4,5,14,15,18,17]
max = 0
second = 0
for i in li:
    if max < i:
        second = max
        max = i
    if max > i and second < i:
        second = i
print(max)
print(second)
'''
'''
li = [2,15,3,4,1,8,6,9,14]

for i in range(1,len(li)-1):
    if li[i] > li[i-1] and li[i] > li[i+1]:
        print(li[i],end = " ")
'''
li = [[1,2,3],[4,5,6],[7,8,9]]
'''
for i in range(len(li)):
    for j in range(len(li[0])):
        print(li[i][j],end = " ")
    print()

for i in range(len(li)):
    for j in range(len(li[0])):
        print(f"{i,j}",end = " ")
    print()

for i in range(len(li)):
    for j in range(i,len(li[0])):
        li[i][j],li[j][i] = li[j][i],li[i][j]

for i in range(len(li)):
    for j in range(len(li[0])):
        print(li[i][j],end = " ")
    print()
'''
max = 0
s = 0
for i in range(len(li)):
    for j in range(len(li[0])):
        if max < li[i][j]:
            s = max
            max = li[i][j]
        if max > li[i][j] and s < li[i][j]:
            s = li[i][j]

print(s)







