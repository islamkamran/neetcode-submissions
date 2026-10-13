class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagram work easy with ascii codes as mentioned that small charater so mean a to z and total 1 to 26 and in loop 0 to 25. so simply we will have two loops inner loop do the work outerloop update the work.
        # innerloop will increment the values of location for each place and we will store this as a list now this list will be a key in a hashmap with will be updated by the outerloop
        # e.g [1,0,0,0,,0....,1] = cat
        # map list = [[cat]]

        # e.g [1,0,0,0,,0....,1] = act
        # map list = [[cat,act]] because the same formation is repeating it self in the loop

        hashmap = defaultdict(list)

        for word in strs:
            # assign the 0-to-26 here
            total_alpha_length = [0]*26

            for char in word:
                total_alpha_length[ord(char)-ord('a')] += 1
            
            hashmap[tuple(total_alpha_length)].append(word)
        
        return list(hashmap.values())
        