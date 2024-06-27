"""n=int(input("enter a no"))
flag=False
if n==1:
    print("not prime")
elif(n>1):
    for i in range(2,n):
        if(n%i==0):
            flag=True
            break
    if flag:
      print(" not prime no")    
    else:
      print("prime no") """       


 #1 to 100   
for i in range(2,101):  
    for j in range(2,101):     
         if(i%j==0):
            break  
    if(i==j):
      print(i)        

   