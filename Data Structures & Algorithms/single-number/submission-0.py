class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check_num = {}
        for num in nums:
            if num in check_num:
                check_num[num] += 1
            else:
                check_num[num] = 1
        
        for key in check_num:
            if check_num[key] == 1:
                return key