# leetcode_AssignCookies

**PROBLEM 1 (Assign Cookies):**
Description:
You’re a parent with cookies to give to children. Each child i has greed factor g[i] (minimum
cookie size to satisfy). Each cookie j has size s[j]. If s[j] ≥g[i], you can assign cookie j to child i.
Maximize the number of content children.

Examples:
Input: g=[1,2,3], s=[1,1] →Output: 1
Explanation: Only one child can be satisfied
Input: g=[1,2], s=[1,2,3] →Output: 2
Explanation: Both children satisfied

Constraints:
1 ≤g.length ≤3 ×104, 0 ≤s.length ≤3 ×104

Hint:
Sort both arrays. Use two pointers. Give smallest cookie that satisfies each child.


**GREEDY CHOICE:**
The goal is to maximize the number of satisfied children, so our greedy choice will be to always give the smallest cookie that can satisfy the least greedy child.


**WHY IT WORKS:**
It works because it ensures that no large cookie is going to be wasted on a child who could've been satisfied with a smaller cookie beforehand. Satisfying the least greedy children with the smallest cookie first, leaving larger cookies available for the greedier children after, makes this the most optimal approach. 


**COMPLEXITY:**
Time: O(n log n + m log m)– since we're sorting two arrays (g and s), and the pointers only pass through each array once.
Space: O(1) – we only use a few variables (i, j, satisfied).
