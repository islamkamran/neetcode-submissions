class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers

        lp, rp = 0, len(s)-1

        while lp < rp:

            while lp < rp and not self.alnum(s[lp]):
                lp += 1
            while rp > lp and not self.alnum(s[rp]):
                rp -= 1
            
            if s[lp].lower() != s[rp].lower():
                return False
            lp, rp = lp + 1, rp - 1
        return True
    
    def alnum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )
    

        