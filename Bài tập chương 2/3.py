# Thông tin công ty và nhân viên
company_name = "GeeksForGeeks Company"
staff_data = [
    {"id": "1", "name": "Amar Pandey", "salary": "8.5 LPA"},
    {"id": "2", "name": "Akbhar Khan", "salary": "6.5 LPA"},
    {"id": "3", "name": "Anthony Walter", "salary": "3.2 LPA"}
]

# Tạo cấu trúc XML dưới dạng chuỗi
xml_data = '<?xml version="1.0"?>\n'
xml_data += "<company>\n"
xml_data += f"    <name>{company_name}</name>\n"

for staff in staff_data:
    xml_data += f"    <staff id=\"{staff['id']}\">\n"
    xml_data += f"        <name>{staff['name']}</name>\n"
    xml_data += f"        <salary>{staff['salary']}</salary>\n"
    xml_data += f"    </staff>\n"

xml_data += "</company>"

# In chuỗi XML ra màn hình
print(xml_data)

# Lưu chuỗi XML vào file
with open("sample.xml", "w", encoding="utf-8") as file:
    file.write(xml_data)
