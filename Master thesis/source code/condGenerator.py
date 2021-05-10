class condGenerator:
    def __init__(self):
        pass
    
    def conditionGeneratorDiscrete(self,attr_name, attr_value):
        return attr_name+"="+ attr_value

    def conditionGeneratorCnts(self, attr_name, attr_value, b):
        if (b == False):
            return attr_name+"<"+ str(attr_value)    
        else:
            return attr_name+">="+ str(attr_value)

    def conditionGeneratorNum(self, attr_name, attr_value, operator):
        return attr_name+operator+ attr_value

    


            

