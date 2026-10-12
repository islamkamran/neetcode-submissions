class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # if the character numbers are same mean they should cancel out so we count them and cancel their count if the count is not cancelled perfectly we False it. put base = 0 from first list add it and from second list delete it or vice versa
        # make the base 0
        count = [0]*26  # mean it a list of 26 zeros and in imigination we are considering 0 as a and 25 as z and how do we actuall find the exact place simple a=97 and each time minus a value ascii from a e.g b=98 so 98-97 = 1 so on index 1 update or increment
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')]-=1
            count[ord(t[i]) - ord('a')]+=1
        
        for i in count:
            if i != 0:
                return False
        
        return True


        