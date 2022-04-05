n = 5
prices = [2,5,7,8,10]

def rod(i,cap):
    if i == 0:
        return cap*prices[0]
    
    nottake = 0 + rod(i-1,cap)
    take = -9999
    rodlength = i+1
    if rodlength<=cap:
        take = prices[i] + rod(i,cap-rodlength)
    
    return max(take,nottake)

print(rod(4,n))



# OUTPUT
# 12
