class Solution:
    def isValid(self, s: str) -> bool:
        lis=[ ]
        for char in s:
            if char in '({[':
                lis.append(char)
            elif char==')':
                if not lis or lis[-1] != '(':
                    return False
                lis.pop()
            elif char=='}':
                if not lis or lis[-1] != '{':
                    return False
                lis.pop()
            elif char==']':
                if not lis or lis[-1] != '[':
                    return False
                lis.pop()
        if len(lis)==0:
            return True
        else:
            return False