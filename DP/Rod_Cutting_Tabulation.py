n = 5
prices = [2,5,7,8,10]
dp2 = [[0 for _ in range(n+1)]for _ in range(n)]

for cap in range(n+1):
    dp2[0][cap] = cap*prices[0]
    
for i in range(1,n):
    for cap in range(n+1):
        nottake = 0 + dp2[i-1][cap]
        take = -9999
        rodlength = i+1
        if rodlength<=cap:
            take = prices[i] + dp2[i][cap-rodlength]
        dp2[i][cap] =  max(take,nottake)
print(dp2[n-1][n])


# OUTPUT
# 12
            
