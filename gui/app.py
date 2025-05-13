import tkinter as tk
import os
import sys
from modules.image_to_pdf import convert_image_to_pdf
from modules.image_to_text import convert_image_to_text
from modules.image_to_word import convert_image_to_word
from modules.pdf_to_word import convert_pdf_to_word
from modules.word_to_pdf import convert_word_to_pdf
from modules.pptx_to_pdf import convert_pptx_to_pdf

import gui.image_to_text_gui.image_to_text_gui as imgToTextGui


def run_app():
    def show_view(func_name, canvas):
        # Xóa vùng view hiện tại
        for widget in view_frame_inner.winfo_children():
            widget.destroy()

        # Tuỳ từng chức năng, tạo UI phù hợp
        if func_name == "Ảnh → PDF":
            tk.Label(view_frame_inner, text="Chức năng: Ảnh → PDF", font=("Arial", 12)).pack()
            tk.Button(view_frame_inner, text="Chọn ảnh và chuyển", command=convert_image_to_pdf).pack(pady=10)

        elif func_name == "Ảnh → Word":
            tk.Label(view_frame_inner, text="Chức năng: Ảnh → Word", font=("Arial", 12)).pack()
            tk.Button(view_frame_inner, text="Chọn ảnh và chuyển", command=convert_image_to_word).pack(pady=10)

        elif func_name == "Ảnh → Text":
            imgToTextGui.convert_image_to_text_ui(view_frame_inner,root)

        elif func_name == "PDF → Word":
            tk.Label(view_frame_inner, text="Chức năng: PDF → Word", font=("Arial", 12)).pack()
            tk.Button(view_frame_inner, text="Chọn file PDF và chuyển", command=convert_pdf_to_word).pack(pady=10)

        elif func_name == "Word → PDF":
            tk.Label(view_frame_inner, text="Chức năng: Word → PDF", font=("Arial", 12)).pack()
            tk.Button(view_frame_inner, text="Chọn file Word và chuyển", command=convert_word_to_pdf).pack(pady=10)

        elif func_name == "PPTX → PDF":
            tk.Label(view_frame, text="Chức năng: PPTX → PDF", font=("Arial", 12)).pack()
            tk.Button(view_frame, text="Chọn file pptx và chuyển", command=convert_pptx_to_pdf).pack(pady=10)

        # Cập nhật kích thước scrollregion của canvas
        view_frame_inner.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    root = tk.Tk()
    root.title("TOOL CHUYỂN ĐỔI FILE")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Đặt kích thước cửa sổ chiếm khoảng 80% chiều rộng và 70% chiều cao
    initial_width = int(screen_width * 0.8)
    initial_height = int(screen_height * 0.8)

    root.geometry(f"{initial_width}x{initial_height}")
    root.resizable(True, True)  # Cho phép thay đổi kích thước cửa sổ

    # Frame bên trái chứa các option
    option_frame = tk.Frame(root, width=200, bg="#f0f0f0")
    option_frame.pack(side="left", fill="y")

    tk.Label(option_frame, text="Chọn chức năng", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=20)

    # Canvas để chứa vùng view có thể cuộn
    canvas = tk.Canvas(root, bg="white", highlightthickness=0)
    canvas.pack(side="right", fill="both", expand=True)

    # Frame bên trong canvas để chứa nội dung
    view_frame_inner = tk.Frame(canvas, bg="white")
    view_frame_inner.pack(fill="both", expand=True)

    # Thanh cuộn dọc
    v_scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    v_scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=v_scrollbar.set)

    # Thanh cuộn ngang (tùy chọn)
    h_scrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    h_scrollbar.pack(side="bottom", fill="x")
    canvas.configure(xscrollcommand=h_scrollbar.set)

    # Đặt view_frame_inner vào canvas
    canvas.create_window((0, 0), window=view_frame_inner, anchor="nw")

    # Cấu hình canvas để có thể cuộn khi nội dung view_frame_inner thay đổi kích thước
    view_frame_inner.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    def on_mouse_wheel(event):
        # Sự kiện cuộn chuột tiêu chuẩn (Windows và một số cấu hình Linux)
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_scroll_event(event):
        # Sự kiện cuộn chuột trên macOS (có thể cần điều chỉnh hệ số)
        canvas.yview_scroll(event.delta, "units")

    # Liên kết sự kiện cuộn chuột
    canvas.bind("<MouseWheel>", on_mouse_wheel)  # Cho Windows và một số Linux
    canvas.bind("<MouseWheel>", on_scroll_event)  # Cho macOS (và có thể cả Linux)

    # canvas.bind("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
    # canvas.bind("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))
    # canvas.bind("<Motion>", lambda event: print(f"Motion: x={event.x}, y={event.y}"))
    # tesst

    options = [
        "Ảnh → PDF",
        "Ảnh → Word",
        "Ảnh → Text",
        "PDF → Word",
        "Word → PDF",
        "PPTX → PDF",
    ]

    for opt in options:
        btn = tk.Button(option_frame, text=opt, width=20, command=lambda o=opt: show_view(o, canvas))
        btn.pack(pady=5)

    def resource_path(relative_path):
        """Trả về đường dẫn thực đến resource (khi đóng gói hoặc chạy dev)"""
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    icon_path = resource_path('assets/icon.ico')
    root.mainloop()