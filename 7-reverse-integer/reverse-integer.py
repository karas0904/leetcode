class Solution:
    def reverse(self, x: int) -> int:
        convert=list(str(x))
        if convert[0]=='-':
            l=1
        else:
            l=0
        r=len(convert)-1
        while l<r:
            temp=convert[l]
            convert[l]=convert[r]
            convert[r]=temp
            l+=1
            r-=1
        reversed_number = int(''.join(convert))
        if reversed_number < -2147483648 or reversed_number > 2147483647:
            return 0
        
        return reversed_number