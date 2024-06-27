#using temp /traditional method
a=10 
b=80
temp=b
b=a
a=temp
print("a",a)
print("b",b)


#without using temp
a=200
b=300
a,b= b,a
print("after swapping the value of a is:",a)
print("after swapping the value of b is:",b)

