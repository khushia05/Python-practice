#Reverse Words in a Given String in Python ram eat mango. mango eat ram
string=str(input("enter the sentence"))
split=string.split(' ')
print(split)
split.reverse()
print(split)
print(' '.join(split))


