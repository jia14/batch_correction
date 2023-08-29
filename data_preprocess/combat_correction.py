import pandas as pd
import argparse
from combat.pycombat import pycombat

# initialize argparse
parser = argparse.ArgumentParser(description='Batch correct csv file')
# add parameters
parser.add_argument('-c', '--csv', type=str, help='The csv file to be processed')
# get all the parameters
args = parser.parse_args()

matrix = pd.read_csv('data/'+args.csv+'.csv')
meta = pd.read_csv('data/meta_integrated.csv')

def process_string(s):
    # Removing the substring before '/'
    s = s.split('/')[-1]
    # Removing '_hist.csv'
    s = s.replace('_hist.csv', '')
    return s
columns_to_drop = []
matrix = matrix.drop(columns=['Unnamed: 0'])
print(matrix)

batch_info = []
for i in range(0,len(matrix.columns)):
    column = matrix.columns[i]
    color = 'black' # Default color
    if 'Cristiano' in column:
        batch_info.append(1)
    elif 'Synder_1' in column:
        batch_info.append(2)
    elif 'radio' in column:
        batch_info.append(3)
    else:
        batch_info.append(0)


matrix_T = matrix.T
corrected_data = pycombat(matrix, batch_info)

corrected_data.to_csv(f'data/batch_c_{args.csv}.csv',index=False)