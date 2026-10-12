class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        # every open must have a closed to be valid and in proper order other wise it is purely false
        # remember when there is a non logic task you have to make some reference function or reference list etc

        stack = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for sign in s:
            if sign in close_to_open:
                if stack and stack[-1] == close_to_open[sign]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sign)
        
        return True if not stack else False


        