class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #a hash of anagram hash: list of words
        #anagram hash: strs: numbers
        # rotate over strs, create hashe, if hash eixts, add it to the ouput
        anagram_list = {}

        for word in strs:
            letter_count = 26*[0]
            for i in range(len(word)):
                letter_count[ord('z')-ord(word[i])] += 1
                
            if tuple(letter_count) in anagram_list:
                anagram_list[tuple(letter_count)].append(word)
            else:
                anagram_list[tuple(letter_count)] = [word]
        
        return list(anagram_list.values())     