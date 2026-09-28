class Solution:
    def isPalindrome(self, s: str) -> bool:
        scopy = ''

        for alpha in s:
            if alpha.isalnum():
                scopy+=alpha.lower()

        if scopy == scopy[::-1]:
            return True
        return False


        