class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]  # the first value
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            mid_point = (left + right) // 2
            result = min(result, nums[mid_point])

            if nums[mid_point] >= nums[left]:
                left = mid_point + 1
            else:
                right = mid_point - 1

        return result