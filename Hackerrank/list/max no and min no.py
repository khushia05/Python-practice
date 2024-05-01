l=[5,90,88,33,2]
max1=l[0]
min1=l[0]
for i in range(len(l)):
    if l[i]>=max1:
        max1=l[i]
    if l[i]<=min1:
        min1=l[i]    
print(max1)
print(min1)       