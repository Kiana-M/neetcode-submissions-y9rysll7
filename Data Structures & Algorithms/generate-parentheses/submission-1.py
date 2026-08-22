class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # opened = ['(']*n
        # closed = [')']*n

        # res = []
        # par = ['(']
        # if len(par)==2*n:
        #     res.append(par)
        # else:
        # first element should always be open paranthesis
        #second element can have two choices
        #third element: if there is an open paranthesis before, 
        #and if the number of open pars are less than n, it can have two choices, ow one choice
        res = []

        def backtrack(path, nopen, nclose):
            if len(path) == 2 * n:
                res.append(path)
                return

            if nopen < n:
                backtrack(path + "(", nopen + 1, nclose)

            if nclose < nopen:
                backtrack(path + ")", nopen, nclose + 1)

        backtrack("", 0, 0)
        return res

            

        