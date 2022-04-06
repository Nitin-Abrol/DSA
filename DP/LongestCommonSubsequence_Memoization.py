s1 = "adebcf"
s2 = "dcadbf"

dp = [[-1 for _ in range(len(s2))]for _ in range(len(s1))]

def longest_subsequence(ind1 , ind2):
    if ind1<0 or ind2<0:
        return 0
      
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
      
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] =  1 + longest_subsequence(ind1-1 , ind2-1)
        return dp[ind1][ind2]
    else:
        dp[ind1][ind2] =  max(longest_subsequence(ind1-1,ind2),longest_subsequence(ind1,ind2-1)) 
        return dp[ind1][ind2]

print(longest_subsequence(5,5))



# Output
# 4
