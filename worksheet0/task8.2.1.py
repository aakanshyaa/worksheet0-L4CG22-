def min_coins(coins, amount):
   
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0: 
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 11
result = min_coins(coins, amount)
print(f"Minimum coins needed to make {amount}: {result}")

