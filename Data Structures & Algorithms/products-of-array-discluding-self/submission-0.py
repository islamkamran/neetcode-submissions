class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to have 3 list:
        # prefix
        # postfix
        # output
        # but we can do all the 3 in the result only first store the prefix and then multiply the postfix to get the output.

        # multiplicative identity
        result = [1] * len(nums)
        prefix = 1 

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range((len(nums)-1), -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result