class Solution:
    def calculate(self, s: str) -> int:
        num, preOp, numStack = 0, "+", []
        
        for elem in s + "+":
            if elem == " ":
                continue
            
            elif elem.isdigit():
                num = num * 10 + int(elem)
            
            else:
                if preOp == "+":
                    numStack.append(num)
                
                elif preOp == "-":
                    numStack.append(-num)
                
                elif preOp == "*":
                    op = numStack.pop()
                    numStack.append(op * num)
                
                elif preOp == "/":
                    op = numStack.pop()
                    numStack.append(math.trunc(op / num))
                
                num, preOp = 0, elem
        
        return sum(numStack)