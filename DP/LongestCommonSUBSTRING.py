# Using Tabulation of Longest Common Subsequence

s1 = "adcd"
s2 = "abzd"

dp2 = [[-1 for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]
for ind2 in range(len(s2)+1):
    dp2[0][ind2] = 0
for ind1 in range(len(s1)+1):
    dp2[ind1][0] = 0

ans = 0
for ind1 in range(1,len(s1)+1):
    for ind2 in range(1,len(s2)+1):
        if s1[ind1-1] == s2[ind2-1]:
            dp2[ind1][ind2] =  1 + dp2[ind1-1][ind2-1]
            ans = max(ans,dp2[ind1][ind2])
        else:
            dp2[ind1][ind2] =  0        # Since there won't be any scene of 

print(dp2)            
print(ans)

# Output
# [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
# 2
