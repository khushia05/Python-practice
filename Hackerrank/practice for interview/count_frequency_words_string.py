# Count the frequency of words appearing in a string Using Python
s1="ram eats mango. shayam eats mango mango"
s=s1.split()
print(s)
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1    
print(count) 