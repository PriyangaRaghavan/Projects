## class to access the training data. Each row is called a Record

from iteration_utilities import unique_everseen

class Records:
    def __init__(self):
        pass
        # self.elements = elements
        # self.index = index
        # self.attrCount = attrCount

    def getRecordElements(self, elements):
        return elements

    def getRecordElementsAtIndex(self, elements, index):
        return elements[index]

    def sizeOfRecords (self, elements):
        return (len(elements))
    
    def totColumns(self, elements):
        return len(self.getRecordElementsAtIndex(elements,0))

    def getRecordValueAtIndex(self, elements, index, attrIndex):
         record = self.getRecordElementsAtIndex(elements, index)
         return record[attrIndex]

    def setRecordAtIndex(self, elements, record, index):
        elements[index] = record
        return elements

    def setRecordValueAtIndex(self, elements, index, attrIndex, value):
        rec =self.getRecordElementsAtIndex(elements, index)
        rec[attrIndex] = value
        return elements

    def swapRecordAtIndexes(self, elements, index1, index2):
        temp1 =self.getRecordElementsAtIndex(elements, index1)
        temp2 =self.getRecordElementsAtIndex(elements, index2)
        temp_elements = self.setRecordAtIndex(elements, temp1, index2)
        elements = self.setRecordAtIndex(temp_elements, temp2, index1)
        return elements
    
    def classAttributeAtIndex(self, elements, index):
        temp=self.getRecordElementsAtIndex(elements, index)
        t = self.totColumns(elements)
        category = temp[t-1]
        return category

    def classAttributes(self,elements):
        size = self.sizeOfRecords(elements)
        #classAttributes =set()
        classAttributes = []
        for i in range(1,size):
            classAttributes.append(self.getRecordValueAtIndex(elements, i, self.totColumns(elements)-1))
        return list(unique_everseen(classAttributes))
        #return list(classAttributes)

    def getClassName(self, elements):
        temp=self.getRecordElementsAtIndex(elements, 0)
        return temp[self.totColumns(elements)-1]
   
    





