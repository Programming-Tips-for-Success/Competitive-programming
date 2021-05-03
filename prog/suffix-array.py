
# A suffix array will contain integers that represent the starting indexes of the all the suffixes of a given string, after the aforementioned suffixes are sorted.

# 0.1.2.3.4.abaab baab aab ab b

# used in areas such as data compression, bioinformatics 
def suffix(s):   
    a = [t[1] for t in sorted((s[i:],i) for i in range(len(s)))]
    print(a)

s='abaab'
suffix(s)