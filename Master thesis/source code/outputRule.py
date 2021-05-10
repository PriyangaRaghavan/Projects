class output:
    def __init__(self):
        pass

    def rule(self,rules: list, classAttr: str):
        l =len(rules)
        string =[]
        for i in range(l+1):
            if i==0:
                string = "IF " + rules[i] 
            elif i==l:
                string = string + " THEN Class is "+ classAttr+ "\n"
            else:
                string = string+" and "+ rules[i]
        
        return string
    


