#find second highest in a list
#[23,55,66,11] o/p=55
lis=list(map(int,input().split()))
print(lis)
lis.sort()
print(lis)
lis.reverse()
print(lis)
print(lis[1])
