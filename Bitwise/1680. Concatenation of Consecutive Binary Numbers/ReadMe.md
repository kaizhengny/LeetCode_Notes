It comes in handy to use bitwise operations when dealing with binary <-> decimal coversions. The main trick is to leftshift the binary bits of n-1 by the bit length of the new number n. Note that to add n to the left shifted bits, you can either use '|' operator or simply '+' n. However, you need to put the bitwise operations in brakets first. It seems math operator '+' has higher priority in the calculation.

    def concatenatedBinary(self, n: int) -> int:
    
        s = 0
        for i in range(1, n+1):
            s = ((s << i.bit_length())+i) % 1000000007

        return s
or     
    
    def concatenatedBinary(self, n: int) -> int:

        s = 0
        for i in range(1, n+1):
            s = (s << i.bit_length() | i) % 1000000007

        return s
        
LeetCode Link https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
