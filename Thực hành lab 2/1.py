import numpy as np

# Bước 1: Tạo Dữ Liệu Mô Phỏng Nhiệt Độ
# Tạo mảng nhiệt độ ngẫu nhiên từ 15 đến 35 độ C cho 30 ngày (số thực)
np.random.seed(42)  # Để đảm bảo kết quả ngẫu nhiên có thể tái lập
temperature_data = np.round(np.random.uniform(15, 35, size=30), 2)

# Tính nhiệt độ trung bình trong tháng
average_temperature = np.mean(temperature_data)
print("Nhiệt độ trung bình trong tháng:", round(average_temperature, 2))

# Bước 2: Phân Tích Xu Hướng Nhiệt Độ
# Tìm ngày có nhiệt độ cao nhất, thấp nhất
max_temp = np.max(temperature_data)
min_temp = np.min(temperature_data)
max_temp_day = np.argmax(temperature_data) + 1  # Ngày bắt đầu từ 1
min_temp_day = np.argmin(temperature_data) + 1

print(f"Ngày có nhiệt độ cao nhất ({max_temp}°C): Ngày {max_temp_day}")
print(f"Ngày có nhiệt độ thấp nhất ({min_temp}°C): Ngày {min_temp_day}")

# Tính sự chênh lệch nhiệt độ giữa các ngày và tìm ngày có sự biến đổi nhiệt độ cao nhất
temp_differences = np.abs(np.diff(temperature_data))
max_difference_day = np.argmax(temp_differences) + 1  # Chênh lệch giữa ngày này và ngày tiếp theo
print(f"Ngày có sự biến đổi nhiệt độ cao nhất: Ngày {max_difference_day} với chênh lệch {temp_differences[max_difference_day-1]:.2f}°C")

# Bước 3: Áp dụng Fancy Indexing
# Lấy các ngày có nhiệt độ cao hơn 20°C
days_above_20 = np.where(temperature_data > 20)[0] + 1
print("Các ngày có nhiệt độ cao hơn 20°C:", days_above_20)

# Lấy nhiệt độ của các ngày 5, 10, 15, 20, 25
selected_days = [5, 10, 15, 20, 25]
selected_temperatures = temperature_data[np.array(selected_days) - 1]
print(f"Nhiệt độ các ngày {selected_days}:", selected_temperatures)

# Tìm nhiệt độ của các ngày có nhiệt độ trên trung bình
above_avg_temperatures = temperature_data[temperature_data > average_temperature]
print("Nhiệt độ các ngày trên trung bình:", above_avg_temperatures)

# Lấy nhiệt độ của các ngày chẵn/lẻ trong tháng
even_days_temperatures = temperature_data[1::2]  # Các ngày chẵn (chỉ số bắt đầu từ 0)
odd_days_temperatures = temperature_data[0::2]   # Các ngày lẻ

print("Nhiệt độ các ngày chẵn:", even_days_temperatures)
print("Nhiệt độ các ngày lẻ:", odd_days_temperatures)
