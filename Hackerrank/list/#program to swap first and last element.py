 #program to swap firstand last element of a list  
#Input : [1, 2, 3]
#Output : [3, 2, 1]
def swaplist(newlist):#M1
    temp= newlist[0]
    newlist[0]=newlist[-1]
    newlist[-1]=temp
    return newlist
newlist=[1,2,3]
print(swaplist(newlist))
#m2

def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))