## class to write output to files

import os.path

class fileWrite:
    def __init__(self):
        pass
    
    def writeRule(self, output):
        f = open("source code\outputFiles\Extracted_Rules.txt", "a")
        f.write(output)
        f.close()

    def writePDDL(self, output):
        f = open("source code\outputFiles\PDDL.txt", "a")
        f.write(output)
        f.close()

    def writeLearnedPredicates(self, output):
        f = open("source code\Evaluation\LearnedPredicates.txt", "a")
        f.write(output)
        f.close()

    def writeNumericalInformation(self, output):
        f = open("source code\Evaluation\ numericalInformation.txt", "a")
        f.write(output)
        f.close()