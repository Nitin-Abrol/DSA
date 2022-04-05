def knap(i,cap):
    if i==0:
        if wt[0]<=cap: return val[0]
        else: return 0
        
    nottake = 0+ knap(i-1,cap)
    take = 0
    if wt[i] <= cap:
        take = val[i] + knap(i-1,cap-wt[i])
    return max(take,nottake)

  
wt = [3,4,5]
val = [30,40,60]
cap = 8

print(knap(2,cap))



#Output
#90
