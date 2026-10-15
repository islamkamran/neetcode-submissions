class Solution:

    def encode(self, strs: List[str]) -> str:
        # strs = ["hello", "world"]
        # list to string
        result_str = ""

        for word in strs:
            result_str += str(len(word)) + "#" + word

        return result_str

    def decode(self, s: str) -> List[str]:
        # s = 5#Hello5#World
        # Key to win is the string limit ;)
        # string to list back and keep track of the loop

        list_words, i = [], 0

        while i < len(s):
            # need to keep track of the word now take out the digit the "#" but remember here the digit is string so simply count the length of characters of digit and by string  conversion make the limit int
            # start j from i here mean i=0 and j=0 next time i=5 so j=5 and so on
            j=i
            while s[j] != "#":
                j += 1
            
            # now we have limit of j lets say 0:2 is j convert to int and append the word to the list_word but remember j is "#" we have to start storing from j+1 till length of the word
            length_of_word = int(s[i:j])

            list_words.append(s[j+1 : j+1 + length_of_word])

            i = j+1 + length_of_word
        return list_words