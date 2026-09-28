class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge case
        if len(s) != len(t):
            return False
        
        # using the Ascii codes

        counts = [0]*26
        for i in range(len(s)):
            counts[ord(s[i])-ord('a')]+=1
            counts[ord(t[i])-ord('a')]-=1

        for value in counts:
            if value != 0:
                return False

        return True

        