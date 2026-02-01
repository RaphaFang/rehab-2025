class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        stack = []
        stack.append(s[0])

        for n in s[1:]:
            if n in {")", "]", "}"}:
                if not stack:
                    return False
                    
                temp = stack.pop()

                if n == ")" and temp == "(":
                    continue
                elif n == "]" and temp == "[":
                    continue
                elif n == "}" and temp == "{":
                    continue
                else:
                    return False
            else:
                stack.append(n)
        if not stack:
            return True
        return False
