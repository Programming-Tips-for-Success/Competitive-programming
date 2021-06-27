'''
You are the manager of a supermarket.
You have a list of
items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items,
The next lines contains the item's name and price, separated by a space.

Output Format
Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation

BANANA FRIES: Quantity bought:
, Price:
Net Price:
POTATO CHIPS: Quantity bought: , Price:
Net Price:
APPLE JUICE: Quantity bought: , Price:
Net Price:
CANDY: Quantity bought: , Price:
Net Price: 
'''

from collections import OrderedDict

n = int(input())
l=OrderedDict()
for i in range(n):
    d=input().split()
    c=d[:-1]
    try:
        l[' '.join(c)]+=int(d[-1])
    except:
        l[' '.join(c)]=int(d[-1])

for i in l.keys():
    print(i,l[i])