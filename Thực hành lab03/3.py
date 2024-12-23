# Đọc file stocks2.csv vào DataFrame
stocks2 = pd.read_csv('stocks2.csv')

# 1. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# 2. Tính giá trị trung bình (mean) của các cột open, high, low, close theo mỗi ngày
average_values = stocks[['open', 'high', 'low', 'close']].mean()
print("\nGiá trị trung bình của các cột:")
print(average_values)

# 3. Hiển thị 5 dòng đầu tiên của kết quả gộp
print("\n5 dòng đầu tiên của DataFrame gộp:")
print(stocks.head())
