'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        start , end = 0, 0

        last_indexs = {letter:idx for idx, letter in enumerate(S)}
        
        for idx, letter in enumerate(S):
            last_idx = last_indexs[letter]
            end = max(end, last_idx)
            
            if idx == end:
                ans.append(end-start+1)
                start = end+1
                
        return ans
        
        
# three pointer solution: start, end and idx
# store the last index of each letter in a map
