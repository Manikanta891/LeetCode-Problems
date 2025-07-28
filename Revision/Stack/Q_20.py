class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        for ele in s:
            if ele in "([{":
                stack.append(ele)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if (top == '(' and ele == ')') or \
                   (top == '[' and ele == ']') or \
                   (top == '{' and ele == '}'):
                    stack.pop()
                else:
                    return False
                    
        return len(stack) == 0
