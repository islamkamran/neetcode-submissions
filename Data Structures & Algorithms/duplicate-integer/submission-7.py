class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using hash_set or set in python
        # by simply comparing the length
        return len(set(nums))<len(nums)
        