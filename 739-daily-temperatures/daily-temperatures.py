class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[ ]
        ans=[0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                n=stack.pop()
                ans[n]=i-n
            stack.append(i)
        return ans