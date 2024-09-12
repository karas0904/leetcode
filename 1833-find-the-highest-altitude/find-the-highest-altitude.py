class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[0] * (len(gain) + 1)
        sums=0
        for i in range(len(gain)):
            sums+=gain[i]
            ans[i+1]=sums
        maxi=max(ans)
        return maxi if maxi>0 else 0
