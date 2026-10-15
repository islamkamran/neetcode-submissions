class Solution:

    def encode(self, strs: List[str]) -> str:
        # list to string
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        # string back to list
        # 5#hello5#world
        list_words, i = [], 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j+=1
            
            LOW = int(s[i:j])
            list_words.append(s[j+1 : j+1 + LOW])

            i = j+1 + LOW
        
        return list_words



