class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force: remove non-alphnumeric characters. reverse the array and see if it is equal to the first array. adds space complexity
        # two pointer: one at the beginning, one at the end
        b = 0
        e = len(s)-1
        while e>b:
            while not s[b].isalnum() and b<e:
                b += 1
            while not s[e].isalnum() and e>b:
                e -= 1
            if s[b].lower() != s[e].lower():
                return False
            else:
                b += 1
                e -= 1
        return True
        