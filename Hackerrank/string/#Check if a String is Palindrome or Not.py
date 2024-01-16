#Check if a String is Palindrome or Not
def pali(name):
   r= ''.join(reversed(name))
   print(r)
   if(name==r):
      print("yes")
   else:
      print("not")


name=str(input("enter a string"))
pali(name)