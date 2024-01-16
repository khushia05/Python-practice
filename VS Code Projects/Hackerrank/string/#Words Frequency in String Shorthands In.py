 #Words Frequency in String Shorthands Input : test_str = 'Gfg is best' 
#Output : {'Gfg': 1, 'is': 1, 'best': 1} 
s='Gfg is best . Geeks are good and Geeks like Gfg'
split=s.split()
r={i:split.count(i) for i in split}
print(r)    #{‘Gfg’: 2, ‘is’: 1, ‘best’: 1, ‘.’: 1, ‘Geeks’: 2, ‘are’: 1, ‘good’: 1, ‘and’: 1, ‘like’: 1}