class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedOpen = {')':'(','}':'{',']':'['}
        
        for char in s:
            if char in closedOpen.values():
                stack.append(char)
            elif char in closedOpen.keys():
                if not stack or stack[-1] != closedOpen[char]:
                    return False
                stack.pop()
        return not stack