n = 5
prices = [2,5,7,8,10]

dp = [[-1 for _ in range(len(prices)+1)]for _ in range(n)]

def rod(i,cap):
    if i == 0:
        return cap*prices[0]
    
    if dp[i][cap]!=-1:
        return dp[i][cap]
    
    nottake = 0 + rod(i-1,cap)
    take = -9999
    rodlength = i+1
    
    if rodlength<=cap:
        take = prices[i] + rod(i,cap-rodlength)
    
    dp[i][cap] =  max(take,nottake)
    return dp[i][cap]
  
print(rod(4,n))

# OUTPUT
# 12
