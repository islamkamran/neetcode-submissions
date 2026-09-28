class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pointer
        lp, rp = 0, len(nums)-1

        while lp <= rp:
            if nums[lp] == target:
                return lp

            if nums[rp] == target:
                return rp

            if nums[lp] < target:
                lp += 1

            if nums[rp] > target:
                rp -= 1
        return -1
        