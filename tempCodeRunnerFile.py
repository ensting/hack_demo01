import tkinter as tk
import random


root = tk.Tk()
root.withdraw()  

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


positions = [(random.randint(0, screen_width - 200), random.randint(0, screen_height - 100)) for _ in range(2)]

def show_message(index):
    """Hiển thị thông báo tại vị trí index trong danh sách positions."""
    if index >= len(positions):
        return 

    x, y = positions[index]
    
    
    msg = tk.Toplevel(root)
    msg.geometry(f"200x100+{x}+{y}")  
    msg.title("Thông báo")

    label = tk.Label(msg, text=f"Thông báo {index + 1}", font=("Arial", 10))
    label.pack(pady=5)
    label2 = tk.Label(msg, text="ensting in here ", font=("Arial", 12))
    label2.pack(pady=10)

   
    button = tk.Button(msg, text="OK", command=lambda: (msg.destroy(), show_message(index + 1)))
    button.pack(pady=10)

    msg.protocol("WM_DELETE_WINDOW", lambda: (msg.destroy(), show_message(index + 1))) 


show_message(0)

root.mainloop()
