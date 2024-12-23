import numpy as np
import pandas as pd

# Bước 1: Đọc Dữ Liệu Từ File CSV
# Đọc file CSV vào DataFrame
file_path = 'diem_hp.csv'  # Đường dẫn đến file CSV
data = pd.read_csv(file_path)

# Hiển thị dữ liệu
print("Dữ liệu đọc từ file CSV:")
print(data)

# Chuyển đổi list này thành một mảng NumPy
grades_array = data.iloc[:, 2:].values  # Lấy các cột điểm (bỏ cột id và tên sinh viên)
print("\nMảng NumPy từ dữ liệu điểm:")
print(grades_array)

# Bước 2: Quy đổi điểm 10 sang điểm tín chỉ
def convert_grade(grade):
    if 8.5 <= grade <= 10:
        return 'A'
    elif 8.0 <= grade < 8.5:
        return 'B+'
    elif 7.0 <= grade < 8.0:
        return 'B'
    elif 6.5 <= grade < 7.0:
        return 'C+'
    elif 5.5 <= grade < 6.5:
        return 'C'
    elif 5.0 <= grade < 5.5:
        return 'D+'
    elif 4.0 <= grade < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng hàm quy đổi điểm
grades_converted = np.vectorize(convert_grade)(grades_array)
print("\nĐiểm quy đổi sang tín chỉ:")
print(grades_converted)

# Bước 3: Phân tích Dữ Liệu theo học phần để phân tích
# Tách dữ liệu điểm theo từng học phần
hp1_grades = grades_array[:, 0]
hp2_grades = grades_array[:, 1]
hp3_grades = grades_array[:, 2]

print("\nĐiểm từng học phần:")
print("HP1:", hp1_grades)
print("HP2:", hp2_grades)
print("HP3:", hp3_grades)

# Phân tích tổng, trung bình, và độ lệch chuẩn
def analyze_grades(grades, hp_name):
    total = np.sum(grades)
    mean = np.mean(grades)
    std_dev = np.std(grades)
    print(f"\nPhân tích học phần {hp_name}:")
    print(f"Tổng: {total:.2f}, Trung bình: {mean:.2f}, Độ lệch chuẩn: {std_dev:.2f}")

analyze_grades(hp1_grades, "HP1")
analyze_grades(hp2_grades, "HP2")
analyze_grades(hp3_grades, "HP3")

# Bước 5: Phân tích tổng hợp
# Tính toán số lượng sinh viên đạt từng loại điểm
unique, counts = np.unique(grades_converted, return_counts=True)
grade_summary = dict(zip(unique, counts))
print("\nSố lượng sinh viên đạt từng loại điểm (A, B+, ...):")
for grade, count in grade_summary.items():
    print(f"Điểm {grade}: {count} sinh viên")
