##class to read attribute files and training data files

import os
import pandas as pd
import csv

class ReadFile:
    def __init__(self):
        pass

    def readAttrFile(self,actionName):
        attrFolderPath = r"source code\Attributes"
        attrFilePaths  = [os.path.join( attrFolderPath, name) for name in os.listdir(attrFolderPath)]
        for path in attrFilePaths:
            if path.find(actionName) != -1:
                    with open(path, 'r') as f:
                        lines = f.readlines()
        return lines
                 
    def readTrainFile(self, actionName):
        trainFolderPath = r"source code\\Training"
        trainFilePaths  = [os.path.join(trainFolderPath, name) for name in os.listdir(trainFolderPath)]
        for path in trainFilePaths:
            if path.find(actionName) != -1:
                with open(path, 'rt') as f:
                    data = csv.reader(f, delimiter=',')
                    elements =[]
                    for row in data:
                        elements.append(row)
        return elements

# test = ReadFile()
# #test.readTrainFile("on_light")
# test.readAttrFile("on_liht")




        




        
        
