class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointers checking from both sides
        # num[i] + num[j] = target
        #  if we sort and check if num[i]+num[j]>target reduce j, if < target increase i
        nc =[]
        for i,num in enumerate(nums):
            nc.append([num,i])

        nc.sort()
        lp, rp = 0, len(nums) - 1  # left and right pointer from start and end
        while lp<rp:
            current = nc[lp][0]+nc[rp][0]

            if current == target:
                val = [min(nc[lp][1],nc[rp][1]),max(nc[lp][1],nc[rp][1])]
                return val
            elif current < target:
                lp+=1
            else:
                rp-=1
        return []


