class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2
            totalHours = 0

            for banana in piles:
                totalHours += math.ceil(float(banana) / k)
            
            if totalHours <= h:
                result = min(result, k)
                # check the remaining as well
                right = k - 1
            else:
                left = k + 1
        return result
