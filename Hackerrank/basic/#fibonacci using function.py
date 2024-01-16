#fibonacci using function with argu no return
def fibo(n):
    a=0
    b=1
    i=2
    print(a)
    print(b)
    while(i<n):
        
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1
n=int(input("enter nth term"));
fibo(n);