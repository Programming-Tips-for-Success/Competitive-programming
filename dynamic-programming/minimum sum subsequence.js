
// JavaScript program to find minimum sum subsequence
// of an array such that one of every four
// consecutive elements is picked.

// Returns sum of minimum sum subsequence
// such that one of every four consecutive
// elements is picked from arr[].

const getMaxProfit = (prices) => {
    let maxProfit = 0;
      
    for (let buyDay = 0; buyDay < prices.length; buyDay++) {
      const buyPrice = prices[buyDay];
  
      for (let sellDay = buyDay + 1; sellDay < prices.length; sellDay++) {
        const sellPrice = prices[sellDay];
        const currentProfit = sellPrice - buyPrice;
  
        maxProfit = Math.max(maxProfit, currentProfit);
      }
    }
  
    return maxProfit;
  };
  console.log(getMaxProfit( [1,1,0, 0]))
  // This code is contributed by code_hunt
  