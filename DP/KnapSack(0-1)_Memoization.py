# ------------ BETTER TIME COMPLEXITY USING MEMOIZATION SOLUTION ------------

wt = [1,2,3]
val = [10,15,40]
cap = 5
def kanp(i,cap):
    if i==0:
        if wt[0]<=cap: return val[0]
        return 0
        
    if dp[i][cap] != -1:
        return dp[i][cap]
    
    nottake = 0+ kanp(i-1,cap)
    take = 0
    if wt[i] <= cap:
        take = val[i] + kanp(i-1,cap-wt[i])
    dp[i][cap] = max(take,nottake)
    return dp[i][cap]
dp = [[-1]*(cap+1)]*3
print(kanp(2,cap))


#OUTPUT
#55
