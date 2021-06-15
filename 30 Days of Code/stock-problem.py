# Find maximum profit earned by buying and selling shares any number of times
# Given a list containing future prediction of share prices, find the maximum profit earned by buying and selling shares any number of times with the constraint, a new transaction can only start after the previous transaction is complete, i.e., we can only hold at most one share at a time.
# Input
# prices = [3,2, 5 ,7, 9] 

# output
# max profit = 5th day sell profit - 7

def maxProfit(price, start, end):
 
    # If the stocks can't be bought
    if (end <= start):
        return 0
 
    # Initialise the profit
    profit = 0
 
    # The day at which the stock
    # must be bought
    for i in range(start, end, 1):
 
        # The day at which the
        # stock must be sold
        for j in range(i+1, end+1):
 
            # If byuing the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
                 
                # Update the current profit
                curr_profit = price[j] - price[i] + maxProfit(price, start, i - 1)+ maxProfit(price, j + 1, end)
 
                # Update the maximum profit so far
                profit = max(profit, curr_profit)
 
    return profit
 

price = [1, 5, 2, 3, 7, 6, 4, 5] 
n = len(price)

print(maxProfit(price, 0, n - 1)) 

# Given a list of stock prices, find maximum profit. You can buy one day and sell on another.

def stockExchange(stockPrices):
    buy = stockPrices[0] 
    sell = 0
    profit = -1
    for n in range(0,len(stockPrices)-1):
        x = stockPrices[n]
        if x < buy:
            buy = x
            sell = 0
        elif x > sell:
            sell = x
            profit = sell - buy
    return profit
def StockPicker(arr):
    bp=0
    sp=0
    mp=-1
    for r in arr:        
        if arr[arr.index(r)+1] > r:
            bp=r
            break
    sp=max(arr[_] for _ in range(arr.index(bp),len(arr)))
    if sp-bp > mp:
        return sp-bp
    else:
        return mp
print(StockPicker([3,2, 5 ,7, 9] ))