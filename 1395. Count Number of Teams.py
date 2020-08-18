# 1395. Count Number of Teams

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """

        asd = 0
        des = 0
        

        for i in range(1,len(rating)-1):
            desl = 0
            asdl = 0
            desr = 0
            asdr = 0
            for j in range(i):
                if rating[j]<rating[i]:
                    asdl +=1
                    
                else:
                    desl +=1
                    
            for k in range(i+1,len(rating)):
                if rating[k]>rating[i]:
                    asdr +=1
                    
                else:
                    desr +=1
                        
            asd += asdl*asdr
            des += desl*desr
            
        return asd + des
                    