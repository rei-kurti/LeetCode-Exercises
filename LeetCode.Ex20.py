
def validString(s: str)->bool:
    ans = list(s)
    if len(ans) % 2 != 0:
        return False
    else:
        for i in range(len(ans)):
            if i == 0 and (ans[i] != '(' or ans[i] != '[' or ans[i] != '{'):
                return False
            if i % 2 != 0 and (ans[i] != '(' or ans[i] != '[' or ans[i] != '{'):
                return False
            if i % 2 == 0 and (ans[i] != ')' or ans[i] != ']' or ans[i] != '}'):
                return False
            if i == len(ans) - 1 and (ans[i] != ')' or ans[i] != ']' or ans[i] != '}'):
                return False
            if ans[i] == '(' and ans[i+1] != ')':
                return False 
            if ans[i] == '[' and ans[i+1] != ']':
                return False 
            if ans[i] == '{' and ans[i+1] != '}':
                return False 
            if ans[i] == ')' and ans[i-1] != '(':
                return False
            if ans[i] == ']' and ans[i-1] != '[':
                return False
            if ans[i] == '}' and ans[i-1] != '{':
                return False
        return True
print(validString("()"))
validString("()[]{}")
validString("(]") #Attribute error