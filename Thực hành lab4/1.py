import sqlite3

# Kết nối tới cơ sở dữ liệu
def connect_db():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    """)
    conn.commit()
    return conn

# Hiển thị danh sách sản phẩm
def display_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    print("\nDanh sách sản phẩm:")
    print("ID | Tên sản phẩm | Giá | Số lượng")
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")

# Thêm sản phẩm mới
def add_product(conn):
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    print("Thêm sản phẩm thành công!")

# Tìm kiếm sản phẩm theo tên
def search_product(conn):
    name = input("Nhập tên sản phẩm cần tìm: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + name + '%',))
    products = cursor.fetchall()
    print("\nKết quả tìm kiếm:")
    if products:
        print("ID | Tên sản phẩm | Giá | Số lượng")
        for product in products:
            print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")
    else:
        print("Không tìm thấy sản phẩm.")

# Cập nhật thông tin sản phẩm
def update_product(conn):
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
    conn.commit()
    print("Cập nhật sản phẩm thành công!")

# Xóa sản phẩm
def delete_product(conn):
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    print("Xóa sản phẩm thành công!")

# Menu giao diện
def menu_gd():
    conn = connect_db()
    while True:
        print("\nChương trình quản lý sản phẩm")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            display_products(conn)
        elif choice == '2':
            add_product(conn)
        elif choice == '3':
            search_product(conn)
        elif choice == '4':
            update_product(conn)
        elif choice == '5':
            delete_product(conn)
        elif choice == '6':
            print("Thoát chương trình.")
            conn.close()
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")
if __name__ == "__menu_gd__":
    menu_gd()
