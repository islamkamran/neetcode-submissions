class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge case
        if len(s) != len(t):
            return False

        # either 1- sort, 2- loop each element and compare or inbuilt function

        return sorted(s) == sorted(t)

        