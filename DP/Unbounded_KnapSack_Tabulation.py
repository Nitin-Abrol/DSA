val = [5,11,13]
wt = [2,4,6]
cap = 10

dp2 = [[0 for _ in range(cap+1)]for _ in range(len(val))]

for W in range(cap+1):
    dp2[0][W] = (W//wt[0])*val[0]

for i in range(1,len(val)):
    for W in range(cap+1):
        nottake = 0 + dp2[i-1][W]
        take = 0
        if wt[i] <= W:
            take = val[i] + dp2[i][W-wt[i]]
        dp2[i][W] = max(nottake,take)

print(dp2[2][cap])



# OUTPUT
# 27
