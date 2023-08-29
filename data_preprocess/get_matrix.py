import argparse
import pandas as pd
import os


# initialize argparse
parser = argparse.ArgumentParser(description='This is a script to transfer csv length into a matix')

# add parameters
parser.add_argument('-f', '--folder', type=str, help='which folder do you like')


# get all the parameters
args = parser.parse_args()

# process the matrix if the input is all
if args.folder == 'all':
        # List of file names
    folder_names = ['Cristiano','Synder_1','radio']
    #folder_names = ['Cristiano','Synder_1']

    # Initialize an empty DataFrame with lengths as index
    matrix = pd.DataFrame(index=range(100, 300))

    # Loop through each file and read the data
    for folder in folder_names:
        file_names = os.listdir('original_data/'+folder)
        for file_name in file_names:
            # Read the file, assuming it has two columns, and no header
            # You can extract just the base name (without the extension) to use as the column name
            column_name = folder + '/' + file_name
            data = pd.read_csv('original_data/'+folder + '/' + file_name, sep=' ', header=None, names=['length', column_name])
            
            # Set the "length" column as the index
            data.set_index('length', inplace=True)
            
            # Join the data to the matrix
            matrix = matrix.join(data)

        # Save the matrix to a CSV file
    matrix.to_csv('data/all_data.csv')
    print(len(matrix.columns))

if args.folder in ['Cristiano','Synder_1','radio']:
    folder = args.folder
        # Initialize an empty DataFrame with lengths as index
    matrix = pd.DataFrame(index=range(100, 300))

    # Loop through each file and read the data

    file_names = os.listdir('original_data/'+folder)
    for file_name in file_names:
        # Read the file, assuming it has two columns, and no header
        # You can extract just the base name (without the extension) to use as the column name
        column_name = folder + '/' + file_name
        data = pd.read_csv('original_data/'+folder + '/' + file_name, sep=' ', header=None, names=['length', column_name])
            
        # Set the "length" column as the index
        data.set_index('length', inplace=True)
            
            # Join the data to the matrix
        matrix = matrix.join(data)

        # Save the matrix to a CSV file
    matrix.to_csv('data/radio.csv')
    print(len(matrix.columns))

else:
    print('You have a typo, Bro!')



