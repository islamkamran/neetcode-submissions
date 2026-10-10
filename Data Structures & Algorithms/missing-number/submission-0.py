class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss = (len(nums) * (len(nums)+1))//2
        total = 0
        for num in nums:
            total+=num
        
        return miss-total