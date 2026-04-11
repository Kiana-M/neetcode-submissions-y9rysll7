# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for op in tokens:
#             if op == '-':
#                 b, a = stack.pop(), stack.pop()
#                 res = b - a
#                 stack.append(res)
#             elif op == '+':
#                 b, a = stack.pop(), stack.pop()
#                 res = b + a
#                 stack.append(res)
#             elif op == '*':
#                 b, a = stack.pop(), stack.pop()
#                 res = b * a
#                 stack.append(res)
#             elif op == "/":
#                 b, a = stack.pop(), stack.pop()
#                 res = int(float(b) / a)
#                 stack.append(res)
#             else:
#                 stack.append(int(op))
#         return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
