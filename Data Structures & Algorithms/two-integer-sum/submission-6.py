class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointers checking from both sides
        # num[i] + num[j] = target
        #  if we sort and check if num[i]+num[j]>target reduce j, if < target increase i
        nums_copy = sorted(nums)
        lp, rp = 0, len(nums_copy)-1
        for i in range(len(nums_copy)):
            if nums_copy[lp]+nums_copy[rp]==target:
                return sorted([lp,rp])
            if nums_copy[lp]+nums_copy[rp]>target:
                rp = rp-1
            if nums_copy[lp]+nums_copy[rp]<target:
                lp = lp+1


