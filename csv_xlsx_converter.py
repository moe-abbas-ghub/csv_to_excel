import pandas as pd

path = '/Users/user.name/Folder/'
input_file = 'input.csv'
path_input_file = path + input_file
output_file = 'output.xlsx'
path_output_file = path + output_file

df = pd.read_csv(path_input_file)

df.to_excel(path_output_file)