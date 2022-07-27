

def suffix(s):   
    a = [t[1] for t in sorted((s[i:],i) for i in range(len(s)))]
    print(a)

s='abaab'
suffix(s)