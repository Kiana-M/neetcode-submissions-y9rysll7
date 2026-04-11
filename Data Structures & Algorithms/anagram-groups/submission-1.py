class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # mapping from a tuple to each word
        # # tuple says how many words each str has
        # anagram_dict = {}
        # for s in strs:
        #     alphabet_list = [0]*26
        #     for char in s:
        #         alphabet_index = ord(char) - ord('a')
        #         alphabet_list[alphabet_index] += 1
            
        #     if tuple(alphabet_list) in anagram_dict:
        #         anagram_dict[tuple(alphabet_list)].append(s)
        #     else:
        #         anagram_dict[tuple(alphabet_list)] = [s]

        # return anagram_dict.values()
        
        #mapping from number of word counts in alphabet: [words]
        res = {}
        for word in strs:
            alpha_list = [0]*26
            for letter in word:
                alpha_list[ord(letter)-ord('a')] += 1
            if tuple(alpha_list) in res:
                res[tuple(alpha_list)].append(word)
            else:
                res[tuple(alpha_list)] = [word]
        return res.values()
                


        

        