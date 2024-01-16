#sum of digit using function
def sum(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    return(s)  
n=int(input("enter a no"))
print("sum of digits",sum(n))  