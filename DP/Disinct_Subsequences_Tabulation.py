s1= "babgbag"
s2 = "bag"
n = len(s1)
m = len(s2)
dp2 = [[0 for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]

for i in range(len(s1)+1):
    dp2[i][0] = 1
for j in range(1,len(s2)+1):
    dp2[0][j] = 0  

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp2[i][j] = dp2[i-1][j-1]+dp2[i-1][j]
        else:
            dp2[i][j] = dp2[i-1][j]
        
print(dp2[n][m])
    
# Output
# 5
