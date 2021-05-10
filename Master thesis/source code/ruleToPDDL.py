## class to convert extracted rules to PDDL

class ruleToPDDL:
    def __init__(self):
        pass

    def prestate(self,rule: list):
        #print(rule)
        string= "precondition: ("
        fluents="precondition: "         ## to extract fluents only to evaluate domain error
        numerical=[]
        for pred in rule:
            if pred.find(">=") != -1:
                temp = pred.split(">=")
                string = string + " (>=(" + temp[0]+")" + temp[1]+")"
                t = "("+temp[0]+") "
                fluents= fluents+t
                numerical.append(temp[1])
            elif pred.find("<") != -1:
                temp = pred.split("<")
                string = string + " (<(" + temp[0]+")" + temp[1]+ ")"
                t = "("+temp[0]+") "
                fluents= fluents+t
                numerical.append(temp[1])
            elif pred.find("=") != -1:
                temp = pred.split("=")
                if temp[1] == "TRUE":
                    string = string +"(" + temp[0]+ ")"
                    t = "("+temp[0]+") "
                    fluents= fluents+t
                else:
                    string = string +"(" + "not("+ temp[0]+ "))"
                    t = "(not("+temp[0]+")) "
                    fluents= fluents+t
        return (string +")"), (fluents),numerical

    def poststate(self,prestate_rule, poststate_rule, function):
        rule = self.diff_prestate_poststate(prestate_rule, poststate_rule)
        string= "effect: ("
        fluents="effect: "        ## to extract fluents only to evaluate domain error
        numerical=[]
        for pred in rule:
            if(function != "None"):
                if pred.find(">=") != -1: 
                    temp = pred.split(">=")
                    string = string + "("+ function + "("+temp[0]+ ")(-("+temp[1]+")("+temp[0]+")))"
                    t = "("+temp[0]+") "
                    fluents= fluents+t
                    numerical.append(temp[1])
                elif pred.find("<") != -1: 
                    temp = pred.split("<")
                    string = string + "("+ function + "("+temp[0]+ ")(-("+temp[1]+")("+temp[0]+")))"
                    t = "("+temp[0]+") "
                    fluents= fluents+t
                    numerical.append(temp[1])
                elif pred.find("=") != -1:
                    temp = pred.split("=")
                    if temp[1] == "TRUE":
                        string = string +"(" + temp[0]+ ")"
                        t = "("+temp[0]+") "
                        fluents= fluents+t
                    else:
                        string = string +"(" + "not("+ temp[0]+ "))"
                        t = "(not("+temp[0]+")) "
                        fluents= fluents+t
            else:
                if pred.find("=") != -1:
                    temp = pred.split("=")
                    if temp[1] == "TRUE":
                        string = string +"(" + temp[0]+ ")"
                        t = "("+temp[0]+") "
                        fluents= fluents+t
                    else:
                        string = string +"(" + "not("+ temp[0]+ "))"
                        t = "(not("+temp[0]+")) "
                        fluents= fluents+t
        return (string +")"),(fluents),numerical
    
    def toReplace(self, string):
        
        if ("not(off-heater)" in string):
            rr= string.replace("(not(off-heater))", "(on-heater)")
       
        elif("(off-heater)" in string):
            rr= string.replace("(off-heater)", "(not(on-heater))")

        elif("not(close)" in string):
            rr= string.replace("(not(close))", "(open)")

        elif("close" in string):
            rr= string.replace("(close)", "(not(open))")

        elif("not(off-light)" in string):
            rr= string.replace("(not(off-light))", "(on-light)")
        
        elif("off-light" in string):
            rr= string.replace("(off-light)", "(not(on-light))")
        return rr
   
    def diff_prestate_poststate(self, prestate_rule, poststate_rule):
        #effect = set(prestate_rule) - set(poststate_rule)
        #print(effect)
        effect = [elem for elem in poststate_rule if elem not in prestate_rule]
        return effect
        

# r = ruleToPDDL()
# rule1= ['on-light=FALSE', 'luminance<353', 'presence=TRUE']
# rule2= ['on-light=TRUE', 'luminance>=570', 'presence=TRUE']
# r.diff_prestate_poststate(rule1, rule2)
# rr=r.replace('(off-heater)')
# print(rr)
# rule = ['off-heater=TRUE', 'temp<23.8']
# o1=r.prestate(rule)
# function = "decrease"
#o1=r.effect(rule, function)
#print(o1)