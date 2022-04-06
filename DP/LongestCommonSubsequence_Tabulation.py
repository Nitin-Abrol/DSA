s1 = "adebcf"
s2 = "dcadbf"

dp2 = [[-1 for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]

for ind2 in range(len(s2)+1):
    dp2[0][ind2] = 0
    
for ind1 in range(len(s1)+1):
    dp2[ind1][0] = 0

for ind1 in range(1,len(s1)+1):
    for ind2 in range(1,len(s2)+1):
        if s1[ind1-1] == s2[ind2-1]:
            dp2[ind1][ind2] =  1 + dp2[ind1-1][ind2-1]
        else:
            dp2[ind1][ind2] =  max(dp2[ind1-1][ind2],dp2[ind1][ind2-1]) 

print(dp2[6][6])


# Output
# 4
