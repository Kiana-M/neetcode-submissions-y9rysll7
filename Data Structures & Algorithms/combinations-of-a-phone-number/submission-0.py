class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        digit_to_letter = {'2':['a','b','c'], '3': ['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p', 'q', 'r', 's'], '8':['t','u','v'], '9':['w','x','y','z']}
        res = []
        path = []
        def backtrack(path, i):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
        
            for letter in digit_to_letter[digits[i]]:
                path.append(letter)
                backtrack(path, i+1)
                path.pop()
        
        backtrack([],0)
        return res

