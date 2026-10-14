class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # solve it by two pointer, safe median and upper limit for handling duplicate
        # step 1 two pointers
        lp, rp = 0, len(nums)

        while lp < rp:
            # step 2 calculate median
            m = lp + ((rp-lp)//2)

            # now checking ht condition to move the pointers move left or right
            if nums[m] > target:
                rp = m
            elif nums[m] <= target:
                lp = m + 1

        return lp-1 if (lp and nums[lp-1] == target) else -1
