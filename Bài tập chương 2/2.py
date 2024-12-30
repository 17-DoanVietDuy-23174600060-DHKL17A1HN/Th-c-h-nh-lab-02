# Danh sách sinh viên
students = [
    {"ID": "001", "Name": "Nguyen Van A", "YearOfBirth": "2000", "Class": "CNTT1", "Gender": "Male"},
    {"ID": "002", "Name": "Tran Thi B", "YearOfBirth": "2001", "Class": "CNTT2", "Gender": "Female"},
    {"ID": "003", "Name": "Le Van C", "YearOfBirth": "2000", "Class": "CNTT1", "Gender": "Male"}
]

# Tạo cấu trúc XML dưới dạng chuỗi
xml_data = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_data += "<Students>\n"

for student in students:
    xml_data += f"    <Student>\n"
    xml_data += f"        <ID>{student['ID']}</ID>\n"
    xml_data += f"        <Name>{student['Name']}</Name>\n"
    xml_data += f"        <YearOfBirth>{student['YearOfBirth']}</YearOfBirth>\n"
    xml_data += f"        <Class>{student['Class']}</Class>\n"
    xml_data += f"        <Gender>{student['Gender']}</Gender>\n"
    xml_data += f"    </Student>\n"

xml_data += "</Students>"

# In chuỗi XML ra màn hình
print(xml_data)

# Lưu chuỗi XML vào file
with open("students.xml", "w", encoding="utf-8") as file:
    file.write(xml_data)
