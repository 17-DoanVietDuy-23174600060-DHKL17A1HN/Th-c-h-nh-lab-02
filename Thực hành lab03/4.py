# Đọc file companies.csv vào DataFrame
companies = pd.read_csv('companies.csv')

# 1. Hiển thị 5 dòng đầu tiên của companies
print("5 dòng đầu tiên của companies:")
print(companies.head())

# 2. Kết hợp stocks và companies dựa trên cột 'symbol'
merged_data = pd.merge(stocks, companies, on='symbol', how='inner')

# 3. Tính giá đóng cửa (close) trung bình cho mỗi công ty
average_close_per_company = merged_data.groupby('symbol')['close'].mean()

# 4. Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình cho mỗi công ty (5 công ty đầu tiên):")
print(average_close_per_company.head())
