class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using hash_set or set in python
        seen_set = set()

        for num in nums:
            if num in seen_set:
                return True
            seen_set.add(num)
        return False
        