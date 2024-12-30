# Thông tin công ty
giam_doc = "Nguyen Van A"
dia_chi = "123 Street, City, Country"
sdt = "0123456789"
ma_so_thue = "123456789"

# Tạo cấu trúc XML dưới dạng chuỗi
xml_data = f"""
<?xml version="1.0" encoding="UTF-8"?>
<Company>
    <Director>{giam_doc}</Director>
    <Address>{dia_chi}</Address>
    <Phone>{sdt}</Phone>
    <TaxCode>{ma_so_thue}</TaxCode>
</Company>
"""

# In chuỗi XML ra màn hình
print(xml_data)

# Lưu chuỗi XML vào file
with open("company_info.xml", "w", encoding="utf-8") as file:
    file.write(xml_data)
