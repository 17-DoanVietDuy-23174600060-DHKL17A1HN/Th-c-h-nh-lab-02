# Bài tập 3
class phan_so:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            print("Mẫu số phải khác 0. Vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def in_phan_so(self):
        print(f"Phân số: {self.tu_so}/{self.mau_so}")

phan_so = phan_so()
phan_so.nhap_phan_so()
phan_so.in_phan_so()
