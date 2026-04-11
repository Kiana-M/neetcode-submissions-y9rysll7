class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        for val in s:
            if val in brackets:
                stack.append(val)
            elif val in brackets.values() and len(stack)>0:
                last_element = stack.pop()
                if brackets[last_element] != val:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        