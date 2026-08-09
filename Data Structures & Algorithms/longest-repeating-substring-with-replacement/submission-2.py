class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for target in set(s):
            w1 = 0
            replacements = 0

            for w2 in range(len(s)):
                if s[w2] != target:
                    replacements += 1

                while replacements > k:
                    if s[w1] != target:
                        replacements -= 1
                    w1 += 1

                longest = max(longest, w2 - w1 + 1)

        return longest