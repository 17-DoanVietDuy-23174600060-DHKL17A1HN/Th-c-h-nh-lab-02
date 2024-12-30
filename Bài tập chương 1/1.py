# Bài tập 1
class HCN:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def in_thong_tin(self):
        print(f"Chiều dài: {self.chieu_dai}""cm")
        print(f"Chiều rộng: {self.chieu_rong}""cm")
        print(f"Chu vi: {self.tinh_chu_vi()}""cm")
        print(f"Diện tích: {self.tinh_dien_tich()}""cm^2")

hinh_chu_nhat = HCN()
hinh_chu_nhat.nhap_du_lieu()
hinh_chu_nhat.in_thong_tin()



