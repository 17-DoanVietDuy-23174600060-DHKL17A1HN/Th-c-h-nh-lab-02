import sqlite3
from tkinter import *
from tkinter import messagebox

# Kết nối cơ sở dữ liệu
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

# Thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    amount = entry_amount.get()

    if name and price and amount:
        cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, float(price), int(amount)))
        conn.commit()
        display_products()
        clear_inputs()
        messagebox.showinfo("Thành công", "Sản phẩm đã được thêm!")
    else:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")

# Hiển thị danh sách sản phẩm
def display_products():
    listbox.delete(0, END)
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        listbox.insert(END, f"ID: {product[0]} | Tên: {product[1]} | Giá: {product[2]} | Số lượng: {product[3]}")

# Tìm kiếm sản phẩm
def search_product():
    listbox.delete(0, END)
    search = entry_name.get()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + search + '%',))
    products = cursor.fetchall()
    if products:
        for product in products:
            listbox.insert(END, f"ID: {product[0]} | Tên: {product[1]} | Giá: {product[2]} | Số lượng: {product[3]}")
    else:
        messagebox.showinfo("Thông báo", "Không tìm thấy sản phẩm!")

# Cập nhật sản phẩm
def update_product():
    selected = listbox.get(ACTIVE)
    if selected:
        product_id = int(selected.split()[1])
        price = entry_price.get()
        amount = entry_amount.get()
        if price and amount:
            cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (float(price), int(amount), product_id))
            conn.commit()
            display_products()
            clear_inputs()
            messagebox.showinfo("Thành công", "Sản phẩm đã được cập nhật!")
        else:
            messagebox.showwarning("Lỗi", "Vui lòng nhập giá và số lượng!")
    else:
        messagebox.showwarning("Lỗi", "Vui lòng chọn sản phẩm để cập nhật!")

# Xóa sản phẩm
def delete_product():
    selected = listbox.get(ACTIVE)
    if selected:
        product_id = int(selected.split()[1])
        cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
        conn.commit()
        display_products()
        messagebox.showinfo("Thành công", "Sản phẩm đã được xóa!")
    else:
        messagebox.showwarning("Lỗi", "Vui lòng chọn sản phẩm để xóa!")
# Xóa các ô nhập
def clear_inputs():
    entry_name.delete(0, END)
    entry_price.delete(0, END)
    entry_amount.delete(0, END)

# Tạo giao diện người dùng
conn = connect_db()
cursor = conn.cursor()

root = Tk()
root.title("Quản lý sản phẩm")
root.geometry("600x400")

# Widgets
Label(root, text="Tên sản phẩm:").grid(row=0, column=0, padx=10, pady=5)
entry_name = Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Giá:").grid(row=1, column=0, padx=10, pady=5)
entry_price = Entry(root)
entry_price.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Số lượng:").grid(row=2, column=0, padx=10, pady=5)
entry_amount = Entry(root)
entry_amount.grid(row=2, column=1, padx=10, pady=5)

Button(root, text="Thêm", command=add_product).grid(row=3, column=0, padx=10, pady=5)
Button(root, text="Tìm kiếm", command=search_product).grid(row=3, column=1, padx=10, pady=5)
Button(root, text="Cập nhật", command=update_product).grid(row=4, column=0, padx=10, pady=5)
Button(root, text="Xóa", command=delete_product).grid(row=4, column=1, padx=10, pady=5)
Button(root, text="Hiển thị tất cả", command=display_products).grid(row=5, column=0, columnspan=2, pady=5)

listbox = Listbox(root, width=80, height=15)
listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

display_products()
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát
conn.close()