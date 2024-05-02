l1=[9,0,5,88,66,33]
l2=[6,0,33,9,22,5]
common=[]
for i in range(len(l1)):
    if l1[i] in l2:
        common.append(l1[i])
print(common)        