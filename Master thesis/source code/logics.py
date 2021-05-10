import Records
import Attributes
import condGenerator
rec = Records.Records()
attr = Attributes.Attributes()
rules = condGenerator.condGenerator()

class logics:
    def __init__(self):
        pass

    def getCountOfCoveredRecords(self, table,value,attrCount):
        s =0
        new_table = []
        for i in range (len(table)):
            if table[i][attrCount] == value:
                new_table.append(rec.getRecordElementsAtIndex(table,i))
                s = s+1
        return new_table, s

    def getCountOfUncoveredRecords(self,table, value, attrCount):
        sum =0
        for i in range (len(table)):
                if table[i][attrCount] != value:
                    sum = sum+1
        return sum

    def recordsContLeft(self, table, attrValue):
        newTable =[] 
        noOfRecCovered=0
        for i in range(1, rec.sizeOfRecords(table)):
            if float(rec.getRecordValueAtIndex(table, i, 1)) < float(attrValue):
                newTable.append(rec.getRecordElementsAtIndex(table, i))
                noOfRecCovered+=1
        #return newTable, noOfRecCovered
        return newTable

    def recordsContRight(self, table, attrValue):
        newTable =[]
        noOfRecCovered=0
        for i in range(1, rec.sizeOfRecords(table)):
            if float(rec.getRecordValueAtIndex(table, i, 1)) >= float(attrValue):
                newTable.append(rec.getRecordElementsAtIndex(table, i))
                noOfRecCovered+=1
        #return newTable, noOfRecCovered
        return newTable
    
    def getCountOfClassValues(self, table, category):
        sum= 0
        for i in range(1,rec.sizeOfRecords(table)):
            if rec.classAttribute(table, i) == category:
                sum =sum+1
        return sum

    def getCountOfOtherClassValues(self, table, category):
        sum= 0
        for i in range(1,rec.sizeOfRecords(table)):
            if rec.classAttribute(table, i) != category:
                sum =sum+1
        return sum

    def listToString(self,lst):
        string = ""
        for i in range(len(lst)):
            string = string+lst[i]+','
        
        return string
    






