# Bài tập 2
class ThiSinh:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0.0
        self.diem_ly = 0.0
        self.diem_hoa = 0.0

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

# Chương trình chính
danh_sach_thi_sinh = []
so_thi_sinh = int(input("Nhập số lượng thí sinh: "))

# Nhập thông tin thí sinh
for _ in range(so_thi_sinh):
    thi_sinh = ThiSinh()
    thi_sinh.nhap_thong_tin()
    danh_sach_thi_sinh.append(thi_sinh)

# Sắp xếp danh sách theo tổng điểm giảm dần
danh_sach_thi_sinh.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)

# In danh sách thí sinh trúng tuyển
diem_chuan = 20.0
print("Danh sách thí sinh trúng tuyển:{n}")
for thi_sinh in danh_sach_thi_sinh:
    if thi_sinh.tinh_tong_diem() >= diem_chuan:
        thi_sinh.in_thong_tin()
        print()
