class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # guass formula n*(n+1)//2
        miss = (len(nums) * (len(nums)+1))//2
        total = 0
        for num in nums:
            total+=num
        
        return miss-total