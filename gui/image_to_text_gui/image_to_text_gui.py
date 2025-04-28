import tkinter as tk
from tkinter import messagebox
from modules.image_to_text import convert_image_to_text

def convert_image_to_text_ui(view_frame):
    def paste_image_and_extract():
        try:
            # Lấy ảnh từ clipboard
            img = ImageGrab.grabclipboard()
            if img is None:
                messagebox.showerror("Lỗi", "Không tìm thấy ảnh trong clipboard!")
                return

            # Trích xuất văn bản từ ảnh
            text = pytesseract.image_to_string(img)

            # Hiển thị kết quả trong Text widget
            text_widget.delete("1.0", tk.END)  # Xóa nội dung cũ
            text_widget.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xử lý ảnh: {str(e)}")

    def upload_and_extract():
        try:
            convert_image_to_text()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xử lý ảnh: {str(e)}")

    # Tạo giao diện cho chức năng
    tk.Label(view_frame, text="Ảnh → Text", font=("Arial", 14, "bold")).pack(pady=10)

    # Nút chọn ảnh từ file
    tk.Button(view_frame, text="Chọn ảnh từ máy tính", command=upload_and_extract).pack(pady=10)

    # Nút dán ảnh từ clipboard
    tk.Button(view_frame, text="Dán ảnh từ clipboard", command=paste_image_and_extract).pack(pady=10)

    # Vùng hiển thị kết quả văn bản
    text_widget = tk.Text(view_frame, height=15, width=70, wrap="word")
    text_widget.pack(pady=10)

    # Nút sao chép kết quả
    def copy_text():
        root.clipboard_clear()
        root.clipboard_append(text_widget.get("1.0", tk.END))
        messagebox.showinfo("Thành công", "Đã sao chép văn bản vào clipboard!")

    tk.Button(view_frame, text="Sao chép văn bản", command=copy_text).pack(pady=10)
