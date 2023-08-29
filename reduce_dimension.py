import argparse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# initialize argparse
parser = argparse.ArgumentParser(description='Use dimension reduction method and show it on plot')
# add parameters
parser.add_argument('-c', '--csv', type=str, help='csv file need to be processed')
parser.add_argument('-m', '--method',type=str,help='the method we need to use')
parser.add_argument('-g', '--group',type=str,help='the group we want to see, if it is folder or healthy/not healthy')

# get all the parameters
args = parser.parse_args()

matrix = pd.read_csv('data/'+args.csv+'.csv')
matrix_t = matrix.iloc[:, 1:].T
#fill up the matrix
matrix_t.fillna(0, inplace=True)
#read the meta dataset
meta = pd.read_csv('data/meta_integrated.csv')


def process_string(s):
    """remove the hist in the name of file to 
    match the meta data.
    """
    # Removing the substring before '/'
    s = s.split('/')[-1]
    # Removing '_hist.csv'
    s = s.replace('_hist.csv', '')
    return s

#get the number of data including tfx in dataset
tfx_list = [0]*len(matrix_t)

for i in range(0,len(matrix.columns)-1):
    column = matrix.columns[i+1]
    #process the file name use the function we defined
    file_name = process_string(column)
    tfx = meta[meta['sample'] == file_name]['tfx']
    if not tfx.empty:
        tfx_list[i]=tfx.item()

#choose the proper dimension reduction method, PCA or T-SNE
if args.method == 'PCA':
    pca = PCA(n_components=2)
    reduced_matrix = pca.fit_transform(matrix_t)

elif args.method == 'T-SNE':
    tsne = TSNE(n_components=2, random_state=42)
    reduced_matrix = tsne.fit_transform(matrix_t)
else:
    print('You have a typo, Bro!')


if args.group == 'tfx':
    # create a dataset
    df = pd.DataFrame(reduced_matrix, columns=["PC1", "PC2"])
    df["label"] = tfx_list

    # show the change of tfx with color
    plt.figure(figsize=(10, 8))
    plt.scatter(reduced_matrix[:, 0], reduced_matrix[:, 1], c=tfx_list, cmap="YlGnBu", s=3)
    cbar = plt.colorbar()
    cbar.set_label('tfx value', rotation=270, labelpad=15)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    #plt.show()
    plt.savefig(f'plot/{args.csv}_{args.method}_{args.group}.png')

elif args.group == 'folder':
    for i in range(0,len(matrix.columns)-1):
        column = matrix.columns[i+1]
        color = 'black' # Default color
        if 'Cristiano' in column:
            dataset = 'Cristiano'
            color = 'red'
        elif 'Synder_1' in column:
            color = 'green'
            dataset = 'Synder_1'
        elif 'radio' in column:
            color = 'purple'
            dataset = 'radio'
        
        # Plot the column with the chosen color
        plt.scatter(x = reduced_matrix[i,0],y = reduced_matrix[i,1], color=color,s=3,label=dataset)
    plt.savefig(f'plot/{args.csv}_{args.method}_{args.group}.png')

else: 
    print('You have a typo, Bro!')

    
