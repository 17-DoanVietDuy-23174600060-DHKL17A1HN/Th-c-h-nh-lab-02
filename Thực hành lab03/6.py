# 1. Tạo Pivot Table từ DataFrame stocks với date làm chỉ mục, symbol làm cột, và giá trị trung bình của close làm giá trị
pivot_table = stocks.reset_index().pivot_table(
    index='date', columns='symbol', values='close', aggfunc='mean'
)

# 2. Hiển thị tổng volume giao dịch của từng chứng khoán (symbol)
total_volume_per_symbol = stocks.groupby('symbol')['volume'].sum()
print("\nTổng volume giao dịch của từng chứng khoán:")
print(total_volume_per_symbol)

# 3. Sắp xếp Pivot Table theo tổng volume giao dịch, từ cao xuống thấp
sorted_symbols = total_volume_per_symbol.sort_values(ascending=False).index
sorted_pivot_table = pivot_table[sorted_symbols]

# 4. Hiển thị Pivot Table đã sắp xếp
print("\nPivot Table đã sắp xếp theo tổng volume:")
print(sorted_pivot_table.head())
