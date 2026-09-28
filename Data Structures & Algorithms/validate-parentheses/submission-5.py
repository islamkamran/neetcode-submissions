class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        # every open must have a closed to be valid and in proper order other wise it is purely false

        stack = []
        # create a reference map
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
            }
        for closing in s:
            if closing in close_to_open:
                if stack and stack[-1] == close_to_open[closing]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(closing)
        
        return True if not stack else False
        