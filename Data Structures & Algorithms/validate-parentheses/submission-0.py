class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        brackets_dict = {')' : '(',']' : '[', '}' : '{'}

        if len(s)%2 == 0:

            for bracket in s:
                
                if bracket == ']' or bracket == '}' or bracket == ')':
                    if not stack:
                        return False

                    if stack[-1] == brackets_dict[bracket]:
                        stack.pop()
                        # print(f'stack after Pop: {stack}')
                    else:
                        return False
                else:
                    stack.append(bracket)
                    # print(stack)

            if len(stack) != 0:
                return False
            
            return True

        return False
