'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

#two pointer solution.
# leave the slow pointer out of the loop and only update it if certen condition is met within the loop. Then iterate the fast pointer through the sting.
# record the largest window size while interation. Silmilar to a DP concept here
# difficult part is really to find out the logic of updating the slow pointer and the help of a dictionary to record the visted item.

def solution(s):
  if len(s)==0: return 0
  s = list(s)
  d = {}
  l = 0
  r = 0
  win_size = 0
  while r < len(s):
    if s[r] not in d:
      d[s[r]] = 1
      r += 1
      win_size=max(win_size, r-l)
    else:
      del d[s[l]]
      l += 1
  return(win_size)

