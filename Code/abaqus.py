import os 
import csv
from odbAccess import openOdb

# Thư mục lưu trữ
save_folder = r"E:\Nghien Cuu Khoa Hoc\Incremental Sheet Forming\Data\RFU_mechanical_data"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Mở ODB 
file_name = "a32_d6_s1000_v500_sto02"

odb_folder = r"E:\Nghien Cuu Khoa Hoc\Incremental Sheet Forming\Mo Phong\Mechanical Simulation\a32_d6_s1000_v500_sto02"
odb_path = os.path.join(
    odb_folder,
    file_name + '.odb'
)

odb = openOdb(odb_path)

# Step mô phỏng 
step_name = list(odb.steps.keys())[-1]
step = odb.steps[step_name]

# Lưu data
save_file = os.path.join(save_folder, file_name + '.csv')

with open(save_file, 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['Time', 'F_z (N)', 'Depth (mm)'])
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
        
        writer.writerow([frame.frameValue, rf3, u3])
        

odb.close()