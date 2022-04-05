dp2 = [[0 for i in range(cap+1)]for j in range(3)]

#BASE CASE
for w in range(wt[0],cap+1):
    dp2[0][w] = val[0]
    
for i in range(1,3):
    for cap in range(0,cap+1):
        nottake = 0 + dp2[i-1][cap]
        take = -999
        if wt[i] <= cap:
            take = val[i] + dp2[i-1][cap-wt[i]]
        dp2[i][cap] = max(take,nottake)
print(dp2)
print(dp2[i][cap])

#Output
#[[0, 10, 10, 10, 10, 10], 
# [0, 10, 15, 25, 25, 25], 
# [0, 10, 15, 40, 50, 55]]
#55
