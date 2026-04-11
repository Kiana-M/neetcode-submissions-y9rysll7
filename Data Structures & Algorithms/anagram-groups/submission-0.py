class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping from a tuple to each word
        # tuple says how many words each str has
        anagram_dict = {}
        for s in strs:
            alphabet_list = [0]*26
            for char in s:
                alphabet_index = ord(char) - ord('a')
                alphabet_list[alphabet_index] += 1
            
            if tuple(alphabet_list) in anagram_dict:
                anagram_dict[tuple(alphabet_list)].append(s)
            else:
                anagram_dict[tuple(alphabet_list)] = [s]

        return anagram_dict.values()

        