import os 
import numpy as np 
import pandas as pd 

# Đường dẫn thư mục 
work_folder = r"E:\Scientific Research\Incremental Sheet Forming\Data" # Thư mục làm việc
input_data_folder = os.path.join(work_folder, "new_clean_cloud_data_mechanical") # Thư mục chứa data đầu vào 
output_data_folder = os.path.join(work_folder, "C2M_data_mechanical") # Thư mục lưu trữ data mới

# Tạo thư mục lưu trữ data mới (nếu chưa có)
if not os.path.exists(output_data_folder):
    os.makedirs(output_data_folder)

# Lọc file CSV
data_files = [f for f in os.listdir(input_data_folder) if f.endswith('.csv')]

for data_file in data_files:
    data_frame = pd.read_csv(os.path.join(input_data_folder, data_file))

    # Min, max C2M
    C2M_min = np.min(np.abs(data_frame['C2M_signed_distances']))
    C2M_max = np.max(np.abs(data_frame['C2M_signed_distances']))

    new_data_frame = data_frame
    new_data_frame.loc[0, 'C2M_min_max'] = C2M_min
    new_data_frame.loc[1, 'C2M_min_max'] = C2M_max
    new_data_frame.rename(
        columns={
            '//X':'X',
            'C2M_signed_distances':'C2M_distances'
        },
        inplace=True
    )

    # Lưu file data
    new_data_frame.to_csv(
        os.path.join(output_data_folder, "C2M_" + data_file),
        index=False
    )