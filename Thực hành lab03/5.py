# 1. Tạo MultiIndex cho DataFrame stocks bằng cách sử dụng cột date và symbol làm chỉ mục
stocks.set_index(['date', 'symbol'], inplace=True)

# 2. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình theo ngày và mã chứng khoán
grouped_data = stocks.groupby(['date', 'symbol']).mean()

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán
sorted_data = grouped_data.sort_index()

# 4. Hiển thị kết quả cho 5 ngày đầu tiên
print("\nKết quả sau khi tính toán và sắp xếp (5 ngày đầu tiên):")
print(sorted_data.head())
