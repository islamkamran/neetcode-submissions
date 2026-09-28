class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)
        # upper bound such that we find the greater index next to the target index-1 is target
        while l < r:
            m = l + ((r-l)//2)

            if nums[m] > target:
                r=m
            elif nums[m] <= target:
                l = m + 1
            
        return l-1 if (l and nums[l-1] == target) else -1
