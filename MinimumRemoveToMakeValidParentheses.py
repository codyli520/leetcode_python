class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, e in enumerate(s):
            if e not in "()":
                continue
            elif e == "(" or not stack:
                stack.append((i, e))
            elif e == ")":
                if stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append((i, e))

        index_to_remove = [e[0] for e in stack]

        res = ""

        for i in range(len(s)):
            if i not in index_to_remove:
                res += s[i]

        return res
