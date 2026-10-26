class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0

        for right in range(len(s)):
            # right pointer store the data until the limit reached and the left pointer remove the data
            # we store the character and the frequency at max we can have 26 charachters with frequency
            # store the charater
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result


        