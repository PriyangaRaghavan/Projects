## class to access attributes of actions

class Attributes:
    def __init__(self):
        pass

    ## function definition to get attribute's name, type and values
    def AttributeParser(self, lines: str):
        mainLine = lines
        split = mainLine.split(':')
        attributeName = split[0]
        if split[1] == "numerical":
            attributeType = "numerical"
            attributeValues = "cnts"
        else:
            attributeType = "logical"
            attributeValues = split[1].split(" ")
        
        return attributeName, attributeType, attributeValues

    def AttributeTable (self, lines: str):
        AttrTable = {}
        for i in range (len(lines)):
            name, typ, values = self.AttributeParser(lines[i].strip())
            AttrTable[i] ={}
            AttrTable[i] ['name'] = name
            AttrTable[i] ['type'] = typ
            AttrTable[i] ['values'] = values
        return AttrTable


    def getName (self, lines, index):
        attrTable = self.AttributeTable(lines)
        attrName = attrTable[index]['name']
        return attrName

    def getType (self, lines,index):
        attrTable = self.AttributeTable(lines)
        attrType = attrTable[index]['type']
        return attrType

    def getValues (self, lines,index):
        index= index
        attrTable = self.AttributeTable(lines)
        attrValues = attrTable[index]['values']
        return attrValues
        
    def numberOfAttributes(self, lines):
        attrTable = self.AttributeTable(lines)
        return (len(attrTable))

    def numberOfValues(self, lines, index):
        index = index
        attrTable = self.AttributeTable(lines)
        if  attrTable[index] ['type'] != "numerical":
            num = len(attrTable[index]['values'])     
        else:
            raise ValueError("Can't give count of continuous values")  
        return num     




