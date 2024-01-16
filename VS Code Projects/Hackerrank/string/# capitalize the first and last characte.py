# capitalize the first and last character of each word in a stringInput: hello world 
#Input: hello world 
#Output: HellO WorlD
s="hello world"
split=s.split()
for i in split:
    change=i[0].upper()+i[1:-1]+i[-1].upper()
    print(change, end=" ")
    # r=' '.join(change) 
    # print(r, end =" ")  