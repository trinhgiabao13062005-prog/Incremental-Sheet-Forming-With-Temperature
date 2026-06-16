import os 
import pandas as pd 

input_dir = r"E:\Scientific Research\Incremental Sheet Forming\Data\clean_cloud_data_mechanical"
output_dir = r"E:\Scientific Research\Incremental Sheet Forming\Data\new_clean_cloud_data_mechanical"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for csv_file in csv_files: 
    input_file = os.path.join(input_dir, csv_file)
    output_file = os.path.join(output_dir, csv_file)

    df = pd.read_csv(input_file, 
                     delim_whitespace=True,
                     index_col=False)
    
    
    df.to_csv(output_file,
              index=False)   