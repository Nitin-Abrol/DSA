val = [5,11,13]
wt = [2,4,6]
cap = 10

def unbounded(i,cap):
    if i == 0:
        return (cap//wt[0])*val[0]
    
    nottake = 0 + unbounded(i-1,cap)
    take = -999999
    if wt[i] <=  cap:
        take = val[i] + unbounded(i,cap-wt[i])
    return max(nottake,take)

print(unbounded(2,cap))


#OUTPUT
#27
