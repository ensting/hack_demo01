import tkinter as tk
import random

# Lấy kích thước màn hình
root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Tạo danh sách 10 vị trí ngẫu nhiên
positions = [(random.randint(0, screen_width - 200), random.randint(0, screen_height - 100)) for _ in range(2)]

def show_message(index):
    """Hiển thị thông báo tại vị trí index trong danh sách positions."""
    if index >= len(positions):
        return  # Dừng khi đã hiển thị đủ 10 thông báo

    x, y = positions[index]
    
    # Tạo cửa sổ thông báo
    msg = tk.Toplevel(root)
    msg.geometry(f"200x100+{x}+{y}")  # Đặt vị trí cửa sổ
    msg.title("Thông báo")

    # Nội dung thông báo
    label = tk.Label(msg, text=f"Thông báo {index + 1}", font=("Arial", 10))
    label.pack(pady=5)
    label2 = tk.Label(msg, text="ensting in here ", font=("Arial", 12))
    label2.pack(pady=10)

    # Nút đóng để mở cửa sổ tiếp theo
    button = tk.Button(msg, text="OK", command=lambda: (msg.destroy(), show_message(index + 1)))
    button.pack(pady=10)

    msg.protocol("WM_DELETE_WINDOW", lambda: (msg.destroy(), show_message(index + 1)))  # Đóng bằng dấu X

# Hiển thị thông báo đầu tiên
show_message(0)

root.mainloop()
