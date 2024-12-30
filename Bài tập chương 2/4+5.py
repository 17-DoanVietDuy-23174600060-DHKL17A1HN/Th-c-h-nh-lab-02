import xml.dom.minidom

file_path = "sample.xml" 
cay_dom = xml.dom.minidom.parse(file_path)

company = cay_dom.documentElement

print(f"Root element: {company.tagName}")
# Lấy danh sách các nhân viên
danh_sach_nhan_vien = cay_dom.getElementsByTagName("staff")

# Duyệt qua từng nhân viên và in ra tên và lương
for nhan_vien in danh_sach_nhan_vien:
    ten = nhan_vien.getElementsByTagName("name")[0].childNodes[0].data
    luong = nhan_vien.getElementsByTagName("salary")[0].childNodes[0].data
    print(f"Tên: {ten}, Lương: {luong}")
