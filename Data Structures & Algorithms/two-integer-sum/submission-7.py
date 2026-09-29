class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointers checking from both sides
        # num[i] + num[j] = target
        #  if we sort and check if num[i]+num[j]>target reduce j, if < target increase i
        nums_copy =[]
        for i,num in enumerate(nums):
            nums_copy.append([num,i])

        lp, rp = 0, len(nums)-1  # left and right pointer from start and end
        while lp<rp:
            if nums_copy[lp][0]+nums_copy[rp][0]==target:
                return sorted([nums_copy[lp][1], nums_copy[rp][1]])
            elif nums_copy[lp][0]+nums_copy[rp][0]<target:
                lp=lp+1
            else:
                rp=rp-1
        
        return []


