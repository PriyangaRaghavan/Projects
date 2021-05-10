## Dataset creation for each action

import pandas as pd

# #read entire dataset
xl = pd.ExcelFile("data.xlsx")
df = xl.parse("Sheet1")

## declare the action names with predicates
action_name = ['heater_on', 'heater_off','open_window', 'close_window', 'on_light']
heater_on = ['on-heater', 'temp', 'temp-threshold-low', 'temp-threshold-high', 'hum-threshold-low', 'hum-threshold-high']
heater_off = ['off-heater', 'temp', 'temp-threshold-low', 'temp-threshold-high', 'hum-threshold-low', 'hum-threshold-high']
open_window = ['open', 'air-quality', 'air-quality-threshold']
close_window = ['close', 'air-quality', 'air-quality-threshold']
on_light = ['on-light', 'luminance', 'lum-threshold']

## appending all actions' predicates as a single list
actions = []
actions.append(heater_on)
actions.append(heater_off)
actions.append(open_window)
actions.append(close_window)
actions.append(on_light)

## create an excel sheet
writer = pd.ExcelWriter('sep_actions.xlsx', engine='xlsxwriter')
writer.save()

##function to write corresponding columns of actions into separate sheets

def write(action_name):
   with pd.ExcelWriter('sep_actions.xlsx', engine= "openpyxl", mode='a') as writer:
        columns.to_excel(writer, sheet_name= action_name, index = False)

## selecting columns corresponding to the particular action
## function call to copy the columns to new sheet
num_actions = len(actions)
for i in range(num_actions):
     columns = df[actions[i]]
     write(action_name[i] )







