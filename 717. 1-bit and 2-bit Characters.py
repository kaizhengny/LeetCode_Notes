'''
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
'''

'''The coding itself is straight forward once I figured out the algorithm. Same with almost every other problem, the key is to find a easy algorithm. From my very limited experience, the process to find it involves thorough observation, taking advantage of all given conditions, testing edge cases, and most importanly, believing there is an clever solution to the problem.

For this question, I started with reading and understanding the question thoroghly. The following part, "The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11)", is a bit confusing at first. But with the context given in the question, it basically means only '0', '10' and '11' could represent a charactor.

Then I walked through couple of easy examples like '0', '00', '10', '100', '1010' to fully understand how to determine if the last charctor is a 1 bit charactor.

Next, I tried to start form the last bit to solve the problem, but it doesn't seem to work. '0' of course is a one-bit charactor. Anything ends with '--00' will be a True(one-bit). but it dosen't get any further from there.

Finally, I started form the beginning and realized any charactor starting with '1' is a two bit charctor, and starting with '0' is a one bit charactor. I followed the idea to iterate through the array with the step size decided by the starting bit. Then all of a sudden, I was thinking if the index would be different after the iteration. I tested the idea with couple of examples and it works fine.
Then, I also tested cases like '0', '10', '00'. Luckly, all these cases are already been covered by the codes.

So, here you go, the codes in python listed below:

Time complexity: O(n)
Space complexity: O(1)
'''

def isOneBitCharacter(bits):
    i = 0
    while i < len(bits)-1:
        if bits[i] == 0:
            i += 1   
        else:
            i += 2
    if i == len(bits):
        return False
    return True
