class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap comparision
        hash_map = {}
        for i,num in enumerate(nums):
            hash_map[num]=i

        for i,num in enumerate(nums):
            remaining = target - num
            if remaining in hash_map and hash_map[remaining] != i:
                return [i,hash_map[remaining]]

        return []