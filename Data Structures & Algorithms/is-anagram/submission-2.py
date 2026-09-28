class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge case
        if len(s) != len(t):
            return False
        
        # frequency of the character we store in the hashmap and compare the maps and check in the results are same True else False
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]]= 1+ countS.get(s[i],0)
            countT[t[i]]= 1+ countT.get(t[i],0)
        
        return countS == countT

        