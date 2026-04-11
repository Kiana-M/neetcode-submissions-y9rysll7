class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #start from the first, record the elements in a set
        #if found duplicate, record the length so far, 
        # move the right pointer one point and remove it from set and add the new left one
        # l = 0
        # max_len = 0
        # dupes = set()
        # for r in range(len(s)):
        #     if s[r] in dupes:
        #         max_len = max(max_len, r-l+1)
        #         dupes.remove(s[l])
        #         l += 1
        #     else:
        #         dupes.add(s[r]) 

        # return max_len
        l,r, max_len = 0, 0, 0
        dupes = set()
        while r < len(s):
            if s[r] in dupes:
                max_len = max(max_len, r-l)
                dupes.remove(s[l])
                l+= 1
            else:
                dupes.add(s[r])
                r += 1
                max_len = max(max_len, r-l)
        return max_len
