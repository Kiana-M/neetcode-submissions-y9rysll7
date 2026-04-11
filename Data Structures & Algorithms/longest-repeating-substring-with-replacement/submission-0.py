class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # a dict to keep the count of all chars in the current window
        # an int to keep the max len of valid substring
        # if len(substr) - count(the most frequent char) < k: valid substr-> update max_len
        # if unvalid substr: slide the window, decrease count
        l,r, max_len = 0, 0, 0
        count = {}
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            if r-l+1 - max(count.values()) <= k:
                max_len = max(max_len, r-l+1)
            else:
                count[s[l]] -= 1
                l+=1
        return max_len
                
        