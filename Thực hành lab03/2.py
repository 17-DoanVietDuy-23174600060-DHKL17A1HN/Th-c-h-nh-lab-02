# 1. Kiểm tra xem stocks1 có dữ liệu Null nào không
print("\nKiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())

# 2. Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
if 'high' in stocks1.columns:
    stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)

# 3. Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
if 'low' in stocks1.columns:
    stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)

# 4. Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý dữ liệu Null:")
stocks1.info()
