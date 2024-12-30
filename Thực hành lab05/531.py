import threading

# Biến shared resource
counter = 0

# Hàm được các thread thực thi
def run_task():
    global counter
    for _ in range(100000):  # Tăng giá trị counter nhiều lần
        counter += 1

def main():
    global counter
    # Reset giá trị counter
    counter = 0

    # Tạo danh sách threads
    threads = []
    for _ in range(5):  # Khởi tạo 5 thread
        thread = threading.Thread(target=run_task)
        threads.append(thread)

    # Bắt đầu các thread
    for thread in threads:
        thread.start()

    # Chờ các thread hoàn thành
    for thread in threads:
        thread.join()

    # Kết quả cuối cùng
    print(f"Giá trị cuối cùng của counter: {counter}")

if __name__ == "__main__":
    main()