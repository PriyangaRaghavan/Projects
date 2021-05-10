## identify action taken place

import pandas as pd
from openpyxl import workbook 
from openpyxl import load_workbook

# #read dataset and get worksheet names
x1 = pd.ExcelFile("sep_actions.xlsx")
sheets = x1.sheet_names
num_sheet = len(sheets)

## create an excel sheet
writer = pd.ExcelWriter('identify_action.xlsx', engine='xlsxwriter')
writer.save()

for j in range (1, num_sheet):
    df = x1.parse(sheets[j])
    num_rows = len(df)     # identify number of rows
    column = df.iloc[:,0]  # select the 1st column

    i= 0
    while (i < df.index[-1]):
        row1 = column.iloc[i]
        row2 = column.iloc[i+1]
        if row1 == False and row2 == True:
             i = i+2
        else:
            up_df = df.drop(i, axis =0, inplace=True)
            i= i+1
        
        if (i == df.index[-1]):
            break
    
    writer = pd.ExcelWriter('identify_action.xlsx', engine='openpyxl', mode='a')
    df.to_excel(writer, sheet_name = sheets[j], index = False)
    writer.save()
