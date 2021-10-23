 
test_str = 'sunny'
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1

print(all_freq)


abc = ['a', 'b', 'c', 'd', 'a', 'b']
data = {}
for i in abc:
    if i in data:
        data[i] = data[i] + 1
    else:
        data[i] = 1

print(data)

abc = [1, 3, 4, 2, 1]
data = {}
for i in abc:
    if i in data:
        data[i] = data[i] + 1
    else:
        data[i] = 1

print(data)

# count frequency of characters