class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += str(len(string)) + '|' + string
            print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        p = 0
        decoded = []
        while p < len(s):
            word_len = ''
            while s[p] != '|':
                word_len += s[p]
                p += 1
            
            word_len = int(word_len)
            decoded.append(s[p+1:p+1+word_len])
            p += word_len + 1

        return decoded
            














    # def encode(self, strs: List[str]) -> str:
    #     singlestr = ''
    #     for s in strs:
    #         singlestr += str(len(s)) + '|' + s 
        
    #     return singlestr

    # def decode(self, s: str) -> List[str]:
    #     decoded = []
    #     p = 0
    #     while p< len(s):
    #         word_count = ''
    #         while s[p] != '|':
    #             word_count += s[p]
    #             p += 1
            
    #         decoded.append(s[p+1:p+1+int(word_count)])
    #         p += 1+int(word_count)

    #     return decoded

            
