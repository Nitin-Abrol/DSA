def mcoins(i,target):
    if i == 0:
        if (target%coin[i] == 0):
            return target/coin[i]
        return 999999
    if dp[i][target]!=-1:
        return dp[i][target]
    nottake = 0 + mcoins(i-1,target)
    take = 999999
    if coin[i] <= target:
        take = 1 + mcoins(i,target-coin[i])
        
    dp[i][target] = int(min(take,nottake))
    return dp[i][target]
 
coin = [4,2,3,1]
target = 91
dp = [[-1 for i in range(target+1)]for j in range(len(coin))]
print(mcoins(len(coin)-1,target))


#OUTPUT
#23
