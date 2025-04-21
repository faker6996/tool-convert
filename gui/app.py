import tkinter as tk
from modules.image_to_pdf import convert_image_to_pdf
from modules.image_to_text import convert_image_to_text
from modules.image_to_word import convert_image_to_word
from modules.pdf_to_word import convert_pdf_to_word
from modules.word_to_pdf import convert_word_to_pdf

def run_app():
    def show_view(func_name):
        # Xóa vùng view hiện tại
        for widget in view_frame.winfo_children():
            widget.destroy()

        # Tuỳ từng chức năng, tạo UI phù hợp
        if func_name == "Ảnh → PDF":
            tk.Label(view_frame, text="Chức năng: Ảnh → PDF", font=("Arial", 12)).pack()
            tk.Button(view_frame, text="Chọn ảnh và chuyển", command=convert_image_to_pdf).pack(pady=10)

        elif func_name == "Ảnh → Word":
            tk.Label(view_frame, text="Chức năng: Ảnh → Word", font=("Arial", 12)).pack()
            tk.Button(view_frame, text="Chọn ảnh và chuyển", command=convert_image_to_word).pack(pady=10)

        elif func_name == "Ảnh → Text":
            tk.Label(view_frame, text="Chức năng: Ảnh → Text", font=("Arial", 12)).pack()
            tk.Button(view_frame, text="Chọn ảnh và chuyển", command=convert_image_to_text).pack(pady=10)

        elif func_name == "PDF → Word":
            tk.Label(view_frame, text="Chức năng: PDF → Word", font=("Arial", 12)).pack()
            tk.Button(view_frame, text="Chọn file PDF và chuyển", command=convert_pdf_to_word).pack(pady=10)

        elif func_name == "Word → PDF":
            tk.Label(view_frame, text="Chức năng: Word → PDF", font=("Arial", 12)).pack()
            tk.Button(view_frame, text="Chọn file Word và chuyển", command=convert_word_to_pdf).pack(pady=10)

    root = tk.Tk()
    root.title("TOOL CHUYỂN ĐỔI FILE")
    root.geometry("700x400")
    root.resizable(False, False)

    # Frame bên trái chứa các option
    option_frame = tk.Frame(root, width=200, bg="#f0f0f0")
    option_frame.pack(side="left", fill="y")

    tk.Label(option_frame, text="Chọn chức năng", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=20)

    options = [
        "Ảnh → PDF",
        "Ảnh → Word",
        "Ảnh → Text",
        "PDF → Word",
        "Word → PDF",
    ]

    for opt in options:
        btn = tk.Button(option_frame, text=opt, width=20, command=lambda o=opt: show_view(o))
        btn.pack(pady=5)

    # Frame bên phải là vùng view
    view_frame = tk.Frame(root, bg="white")
    view_frame.pack(side="right", fill="both", expand=True)


    root.iconbitmap('icon.ico')  # Đặt biểu tượng cho cửa sổ
    # Bắt đầu giao diện
    root.mainloop()
