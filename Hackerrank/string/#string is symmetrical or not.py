#string is symmetrical or not khokho half match
name=str(input("enter a string"))
half=int(len(name)/2)
first=name[:half]
second=name[half:]
if(first==second):
    print("yes")
else:
    print("no")    
