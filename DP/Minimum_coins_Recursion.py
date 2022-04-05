def mcoins(i,target):
    if i == 0:
        if (target%coin[i] == 0):
            return target/coin[i]
        return 999999
    
    nottake = 0 + mcoins(i-1,target)
    take = 999999
    if coin[i] <= target:
        take = 1 + mcoins(i,target-coin[i])
    return int(min(take,nottake))

coin = [4,2,3,1]
target = 91
print(mcoins(3,target))

#OUTPUT
#23
