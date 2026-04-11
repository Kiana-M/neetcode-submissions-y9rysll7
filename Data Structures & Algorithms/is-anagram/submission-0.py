class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash, thash = {}, {}
        for char in s:
            if char in shash:
                shash[char] += 1
            else:
                shash[char] = 1
        
        for char in t:
            if char in thash:
                thash[char] += 1
            else:
                thash[char] = 1
        
        if shash == thash:
            return True
        else:
            return False
        