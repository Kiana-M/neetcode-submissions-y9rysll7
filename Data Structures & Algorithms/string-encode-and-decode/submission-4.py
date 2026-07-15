class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += str(len(string)) + '#' + string

        return encoded


    def decode(self, s: str) -> List[str]:
        l, h = 0,0
        decoded = []
        while h<len(s):
            while s[h] != '#':
                h += 1
            length = int(s[l:h])
            decoded.append(s[h+1:h+1+length])
            l = h+1+length
            h = l+1
        return decoded
