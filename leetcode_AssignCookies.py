def findChildren(g, s): # this function finds the maximum number of children that can be satisfied with the given cookies; g is greed factor and s is cookie size

    g.sort()
    s.sort() # we then sort both lists to use a greedy approach, starting from the smallest greed factor and cookie size

    i = 0 # pointer for children
    j = 0 # pointer for cookies
    satisfied = 0 # number of satisfied children

    # we'll iterate through both lists to find matches
    while i < len(g) and j < len(s): 
        if s[j] >= g[i]: # if the current cookie can satisfy the current child
            satisfied += 1 # we increment the count of satisfied children
            i += 1 # move to the next child
        j += 1 # move to the next cookie regardless of whether the child was satisfied or not
    return satisfied # return the total number of satisfied children

# Using the example test cases below, shows us it follows through correctly
print(findChildren([1, 2, 3], [1, 1])) 
print(findChildren([1,2], [1,2,3])) 
