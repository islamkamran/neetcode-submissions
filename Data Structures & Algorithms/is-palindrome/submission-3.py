class Solution:
    def isPalindrome(self, s: str) -> bool:
        # as it from both side same so we can check from both the side lets try two pointers

        lp, rp = 0, len(s)-1

        # if the pointers cross each other we end the loop and remember with two pointers while is best remember the principle of loop check -> work -> increment

        while lp < rp:
            # as there may be other then alpha numeric so we need to ignore that and check the main course if the lp is non alphanum pass it and lp+1 if right is non alphanum pass it and rp-1. Now there could be multiple non aplha in a row we need to check that also but take care while ignoring them did we cross the lp and rp??
            
            while lp < rp and not self.alnum(s[lp]):
                lp += 1
            while rp > lp and not self.alnum(s[rp]):
                rp -= 1
            
            if s[lp].lower() != s[rp].lower():
                return False
            lp, rp = lp+1, rp-1
        
        return True

    def alnum(self, character):
        # check if the value of the character is in the range of the ascii of the A-Z, a-z and 0-9
        return (
        ord('A') <= ord(character) <= ord('Z') or
        ord('a') <= ord(character) <= ord('z') or
        ord('0') <= ord(character) <= ord('9')
        )
        