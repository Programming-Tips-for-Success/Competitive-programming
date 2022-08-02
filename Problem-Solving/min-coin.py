# coin problem

# problem statement
# coins available- 100, 50, 25, 10, 5, 1
# find minimum coins we needed for exchange

# input 273
# output 8 coins (100, 100, 50, 10,10, 1, 1 ,1)
# Algo 
# create array of available coins
# run loop
# find max coin first by dividing the total amount (273/100 = 2)
# subtract amount

# code 

def findCoin(num):
    coins = [ 100, 50, 25, 10, 5, 1]
    count = 0
    for i in range(0, len(coins)):
        number = (num // coins[i]) 
        num = num - (coins[i] * number)
        count = count + number
    print(count)


findCoin(112)