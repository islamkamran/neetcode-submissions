class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap comparision
        hash_map = {}

        for i,num in enumerate(nums):
            remaining = target - num
            if remaining in hash_map:
                return [hash_map[remaining],i]
            hash_map[num]=i
        return []