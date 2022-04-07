# Count the number of ways in which string s2 occurs in string s1
# RECURSION
def count(i,j):
    if j<0:return 1
    if i<0:return 0
    if s1[i] == s2[j]:
        return count(i-1,j-1)+count(i-1,j)  
    else:
        return count(i-1,j)
    
s1= "babgbag"
s2 = "bag"
print(count(len(s1)-1,len(s2)-1))

# Output
# 5
