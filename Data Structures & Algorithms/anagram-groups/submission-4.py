class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordmap = {}
        for word in strs:
            anagram_lst = [0]*26
            for char in word:
                anagram_lst[ord(char)-ord('a')] += 1
            if tuple(anagram_lst) in wordmap:
                wordmap[tuple(anagram_lst)].append(word)
            else:
                wordmap[tuple(anagram_lst)] = [word]
        return list(wordmap.values())
        

        