class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # added a comment to check the compiler of neetcode
        # added a 2nd comment to check the compiler of neetcode
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                    return True
        return False
        