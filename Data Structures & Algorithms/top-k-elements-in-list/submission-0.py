class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # goals
        # 1- Find the count of elements using hashmap that is easy.
        # 2- find there frequency and map them initial the frequency indices with empty [] so we can add the occurance elements

        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # n, c in count = 7:2 7 is element and 2 is sum of occurances
        for n, c in count.items():
            # frequency[2].append(7) mean append the 7 to index 2 so we know 7 has occured 2 times a bit change of bucket problem
            frequency[c].append(n)
        
        result = []  # now taking the result the top occurance must we start the array checking from big size. decending order

        # start from the last go to 0 and reverse (final, 0 , -1)
        for elements in range(len(frequency) - 1, 0, -1):
            for element in frequency[elements]:
                result.append(element)
                if len(result) == k:
                    return result
