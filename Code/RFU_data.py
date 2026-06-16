import os 
import csv
from odbAccess import openOdb

# Thư mục lưu các folder mô phỏng 
parent_folder = r"E:\Nghien Cuu Khoa Hoc\Incremental Sheet Forming\Mo Phong\Temperature Simulation"

# Thư mục lưu data
save_name = "RFU_temperature_data" 
save_path = r"E:\Nghien Cuu Khoa Hoc\Incremental Sheet Forming\Data"
save_folder = os.path.join(
    save_path, save_name
)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Các thư mục mô phỏng 
work_folders = os.listdir(parent_folder)

# Lọc file odb
file_names = []
odb_paths = []
for work_folder in work_folders:
    for file in os.listdir(os.path.join(parent_folder,work_folder)):
        if file.endswith('.odb'):
            # Lấy tên file odb (đặt tên file csv)
            file_name = file
            file_names.append(file_name.replace('.odb', ''))

            odb_paths.append(
                os.path.join(parent_folder, 
                             work_folder, 
                             file)
            )

# Lưu file csv
for odb_file, file_name in zip(odb_paths, file_names):
    # Mở file odb
    odb = openOdb(odb_file)
    step = odb.steps[list(odb.steps.keys())[-1]]

    save_file = os.path.join(save_folder, file_name + '.csv')
    if not os.path.exists(save_file):
        with open(save_file, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(['Time', 'Depth (mm)', 'F_z (N)'])
            for frame in step.frames:
                rf = frame.fieldOutputs['RF'] # Phản hồi lực
                u = frame.fieldOutputs['U'] # Đọ sâu

                rf3 = 0
                u3 = 0 

                # Lọc giá trị phản hồi lực 
                for r in rf.values: 
                    if r.nodeLabel == 1:
                        rf3 = r.dataDouble[2]
                        break
                
                # Lọc giá trị độ sâu
                for d in u.values: 
                    if d.nodeLabel == 1:
                        u3 = d.dataDouble[2]
                        break
                
                writer.writerow([frame.frameValue, u3, rf3])