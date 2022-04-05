val = [5,11,13]
wt = [2,4,6]
cap = 10

dp = [[-1 for _ in range(cap+1)]for _ in range(len(val))]

def unbounded(i,cap):
    if i == 0:
        return (cap//wt[0])*val[0]
    if dp[i][cap]!=-1:
        return dp[i][cap]
    nottake = 0 + unbounded(i-1,cap)
    take = -999999
    if wt[i] <=  cap:
        take = val[i] + unbounded(i,cap-wt[i])
    dp[i][cap] = max(nottake,take)
    return  dp[i][cap]
  
print(unbounded(2,cap))


# OUTPUT
# 27
