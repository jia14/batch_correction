# Preprocess: get_matrix.py


The `get_matrix.py` script located in the "preprocess" folder is designed to fetch and preprocess cf-DNA data from various files. The processed data is organized into a matrix where each row corresponds to a cf-DNA file name and each column represents the length of cf-DNA.



Navigate to the preprocess folder and run the script with the following command:

```bash
python get_matrix.py -f all
```
The `standize_matrix.py` is a script to standardize the file, change the length of each file into percentage.

To run the script:
```bash
python standize.py -c file.csv
```
And the script combat_correction.py is used to correct batch errors.

The script `reduce_dimension.py` is used to visulize the result of dimension reduce. The parameters include the file we want to visulize, the method we will use to do dimension reduction and the label we want to use to visulize the data(including tfx value and the dataset).

To run the script:
```bash
python reduce_dimension.py -c file.csv -m PCA -g tfx
```
And the plot can be saved in the folder plot.