class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n != 1 and n != 4:
            count = 0
            for digit in str(n):
                count += int(digit) ** 2
            n = count    
        return n == 1
