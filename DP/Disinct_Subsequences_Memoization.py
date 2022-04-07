# MEMOIZATION
def count(i,j):
    if j<0:
        return 1
    if i<0:return 0
    if dp[i][j] !=-1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = count(i-1,j-1)+count(i-1,j)
        return dp[i][j]
    else:
        dp[i][j] = count(i-1,j)
        return dp[i][j]
    
s1= "babgbag"
s2 = "bag"
dp = [[-1 for _ in range(len(s2))]for _ in range(len(s1))]
print(count(len(s1)-1,len(s2)-1))


# Output
# 5
