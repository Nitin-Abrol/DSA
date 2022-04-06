s1 = "adebcf"
s2 = "dcadbf"

def longest_subsequence(ind1 , ind2):
    if ind1<0 or ind2<0:
        return 0
    
    if s1[ind1] == s2[ind2]:
        return 1 + longest_subsequence(ind1-1 , ind2-1)
    
    return max(longest_subsequence(ind1-1,ind2),longest_subsequence(ind1,ind2-1)) 


print(longest_subsequence(5,5))


# Output
# 4
