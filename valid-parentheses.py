class Solution:
    def isValid(self, s: str) -> bool:
        fullStack = []
        brackets = {'(': ')', '[':']', '{':'}'} 
        for i in s:
            if  i in brackets.keys():
                fullStack.append(i)
             
            else:
                if fullStack:
                    brk = fullStack.pop() 
                    if i != brackets[brk]:
                        return False 
                else:
                    return False
        
        if len(fullStack):
            return False
        return True    

            
                
            
        
