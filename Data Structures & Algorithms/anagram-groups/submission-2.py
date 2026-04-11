class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
                


        

        