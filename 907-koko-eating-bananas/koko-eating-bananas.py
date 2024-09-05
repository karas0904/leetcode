class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(k):
            hours=0
            for pile in piles:
                hours+=ceil(pile/k)
            return hours<=h

        l=1
        r=max(piles)

        while(l<r):
            mid=(l+r)//2

            if time_taken(mid):
                r=mid
            else:
                l=mid+1
        return l

        