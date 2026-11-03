class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # guass formula x = n*(n+1)/2 => x-sumofnums => Missing Numbers

        x = (len(nums) * (len(nums)+1))//2

        sum_nums = 0
        for num in nums:
            sum_nums += num
        
        return x-sum_nums