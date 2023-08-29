import pandas as pd
import argparse


# initialize argparse
parser = argparse.ArgumentParser(description='This is a script to transfer standize csv')

# add parameters
parser.add_argument('-c', '--csv', type=str, help='the csv file you want to standize')

# get all the parameters
args = parser.parse_args()

csv_name = args.csv

matrix = pd.read_csv('data/'+csv_name+'.csv')
for column in matrix.columns[1:]:
    for i in matrix[column]:
        column_sum = matrix[column].sum()
    
        # Divide each element in the column by the sum
        matrix[column] = matrix[column] / column_sum

matrix.fillna(0, inplace=True)
matrix.to_csv(f'data/{csv_name}_standard.csv',index=False)