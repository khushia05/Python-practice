""" Anagram”
     Explanation: All characters of “listen” and “silent” are the same.
    Input : s1 = "listen"
        s2 = "silent"
     Output : The strings are anagrams."""
s1="listen"
s2="silento"
print(sorted(s1))
print(sorted(s2))
if sorted(s1)==sorted(s2):
   print("yes")
else:
   print("not")   