dp2 = [[0 for i in range(target+1)]for j in range(len(coin))]
coin = [3,2,4,1]
target = 21

for tar in range(target+1):
    if tar%coin[0] == 0:
        dp2[0][tar] =  int(tar/coin[0])
    else:
        dp2[0][tar] = 999999

for i in range(1,len(coin)):
    for tar in range(target+1):
        nottake = 0 + dp2[i-1][tar]
        take = 999999
        if coin[i] <= tar:
            take = 1 + dp2[i][tar-coin[i]]
            
        dp2[i][tar] = int(min(take,nottake))
        
print(dp2[3][target])

#OUTPUT
#6
