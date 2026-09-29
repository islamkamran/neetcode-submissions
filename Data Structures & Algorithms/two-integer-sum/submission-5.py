class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointers checking from both sides
        # num[i] + num[j] = target
        #  if we sort and check if num[i]+num[j]>target reduce j, if < target increase i

        lp, rp = 0, len(nums)-1
        nums.sort()
        for i in range(len(nums)):
            if nums[lp]+nums[rp]==target:
                return sorted([lp,rp])
            if nums[lp]+nums[rp]>target:
                rp = rp-1
            if nums[lp]+nums[rp]<target:
                lp = lp+1


