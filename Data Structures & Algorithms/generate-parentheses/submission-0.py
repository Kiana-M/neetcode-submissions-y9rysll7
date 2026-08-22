class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, nopen, nclose):
            if len(path)==2*n:
                res.append(path)
                return
            
            for choice in ['(', ')']:
                if choice == '(' and nopen>=n:
                    continue
                if choice == ')' and nclose>=nopen:
                    continue
                
                path += choice
                if choice == '(':
                    nopen +=1
                if choice == ')':
                    nclose +=1
                backtrack(path, nopen, nclose)
                path=path[:len(path)-1]

                if choice == "(":
                    nopen -= 1
                else:
                    nclose -= 1


        backtrack('',0,0)
        return res


                
            

        