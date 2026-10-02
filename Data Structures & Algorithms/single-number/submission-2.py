class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ^ us used for XOR and everything that is XOR with 0 = that value n ^ 0 = n, 1 ^ 0 = 1, 0 ^ 0 =
        #  0 so we start from Xoring with 0

        result = 0

        for num in nums:
            result = num ^ result
        
        return result