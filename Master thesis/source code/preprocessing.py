## Preporocessing techniques

import numpy as np
import matplotlib.pyplot as plt

class preprocessing:
    def __init__(self):
        pass

    ## function to discretize
    def discretize(self,data_list, number_class):
        data_list.sort()
        mat1 = []
        for i in range(len(data_list) + 1):
            temp = []
            for j in range(number_class + 1):
                temp.append(0)
            mat1.append(temp)
        mat2 = []
        for i in range(len(data_list) + 1):
            temp = []
            for j in range(number_class + 1):
                temp.append(0)
            mat2.append(temp)
        for i in range(1, number_class + 1):
            mat1[1][i] = 1
            mat2[1][i] = 0
            for j in range(2, len(data_list) + 1):
                mat2[j][i] = float('inf')
        v = 0.0
        for l in range(2, len(data_list) + 1):
            s1 = 0.0
            s2 = 0.0
            w = 0.0
            for m in range(1, l + 1):
                i3 = l - m + 1
                val = float(data_list[i3 - 1])
                s2 += val * val
                s1 += val
                w += 1
                v = s2 - (s1 * s1) / w
                i4 = i3 - 1
                if i4 != 0:
                    for j in range(2, number_class + 1):
                        if mat2[l][j] >= (v + mat2[i4][j - 1]):
                            mat1[l][j] = i3
                            mat2[l][j] = v + mat2[i4][j - 1]
            mat1[l][1] = 1
            mat2[l][1] = v
        k = len(data_list)
        kclass = []
        for i in range(number_class + 1):
            kclass.append(min(data_list))
        kclass[number_class] = float(data_list[len(data_list) - 1])
        count_num = number_class
        while count_num >= 2: 
            idx = int((mat1[k][count_num]) - 2)
            kclass[count_num - 1] = data_list[idx]
            k = int((mat1[k][count_num] - 1))
            count_num -= 1
        return kclass

## function to find difference between prestate and poststate values
    def diff_in_numerical_attr(self, num_val):
        j=0
        d=[]
        for i in range(int(len(num_val)/2)):
            d.append(float(num_val[j]) - float(num_val[j+1]))
            j=j+2
            
        count_neg=0
        count_pos=0
        for i in range(len(d)):
            if(d[i]<0):
                count_neg = count_neg+1
            else:
                count_pos=count_pos+1

        if(count_pos>count_neg):
            operator = ">="  
            function = "decrease"
        else:
            operator = "<"  
            function = "increase"
        return operator,function


