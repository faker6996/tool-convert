import tkinter as tk
import pytesseract
from tkinter import messagebox, Label
from PIL import Image, ImageGrab, ImageTk

def convert_image_to_text_ui(view_frame, root):

    def resize_image_proportional(image, container_width, container_height):
        """Resize ảnh PIL theo tỷ lệ để vừa với container."""
        if not image:
            return None

        img_width, img_height = image.size

        if img_width <= container_width and img_height <= container_height:
            return image  # Ảnh đã đủ nhỏ

        width_ratio = container_width / img_width
        height_ratio = container_height / img_height

        if width_ratio < height_ratio:
            new_width = int(img_width * width_ratio)
            new_height = int(img_height * width_ratio)
        else:
            new_width = int(img_width * height_ratio)
            new_height = int(img_height * height_ratio)

        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def paste_image_and_extract():
        try:
            img = ImageGrab.grabclipboard()
            if img is None:
                messagebox.showerror("Lỗi", "Không tìm thấy ảnh trong clipboard!")
                image_label.config(image=None)
                image_label.image = None
                text_widget.delete("1.0", tk.END)
                return
            print('Đã dán ảnh từ clipboard')

            # Lấy kích thước của image_label
            label_width = image_label.winfo_width()
            label_height = image_label.winfo_height()

            # Resize ảnh theo tỷ lệ để vừa với image_label
            resized_img = resize_image_proportional(img, label_width, label_height)

            if resized_img:
                img_tk = ImageTk.PhotoImage(resized_img)
                image_label.config(image=img_tk)
                image_label.image = img_tk
            else:
                image_label.config(image=None)
                image_label.image = None
            print('Đã resize ảnh theo tỷ lệ')

            # Trích xuất văn bản từ ảnh gốc (không resize cho OCR)
            text = pytesseract.image_to_string(img)
            print('Đã trích xuất văn bản từ ảnh',text)

            # Hiển thị kết quả văn bản
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, text)

            print('Đã hiển thị văn bản')

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xử lý ảnh từ clipboard: {str(e)}")
            image_label.config(image=None)
            image_label.image = None
            text_widget.delete("1.0", tk.END)

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

    # Tạo frame chứa ô text và ô ảnh (layout mới)
    content_frame = tk.Frame(view_frame, bg="lightgray") # Màu nền để dễ nhìn
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Ô text (chiếm 2 phần)
    text_label = tk.Label(content_frame, text="Văn bản đã detect được:", anchor="w")
    text_label.grid(row=0, column=0, sticky="ew")
    text_widget = tk.Text(content_frame, height=15, wrap="word", bg="white", fg="black")
    text_widget.grid(row=1, column=0, sticky="nsew", padx=(0, 5), pady=(0, 10)) # Thêm padding dưới

    # Ô hiển thị ảnh (chiếm 8 phần)
    image_label_title = tk.Label(content_frame, text="Ảnh đã chọn:", anchor="w")
    image_label_title.grid(row=0, column=1, sticky="ew")
    image_label = tk.Label(content_frame, text="[Ảnh sẽ hiển thị ở đây]", relief="sunken") # Placeholder
    image_label.grid(row=1, column=1, sticky="nsew", padx=(5, 0), pady=(0, 10)) # Thêm padding dưới

    # Cấu hình weight của cột để phân chia không gian
    content_frame.grid_columnconfigure(0, weight=2) # Cột 0 (text) chiếm 2 phần
    content_frame.grid_columnconfigure(1, weight=8) # Cột 1 (ảnh) chiếm 8 phần
    content_frame.grid_rowconfigure(1, weight=1) # Cho phép text_widget và image_label mở rộng theo chiều dọc

    # Nút sao chép kết quả
    def copy_text():
        root = view_frame.winfo_toplevel()
        root.clipboard_clear()
        root.clipboard_append(text_widget.get("1.0", tk.END))
        messagebox.showinfo("Thành công", "Đã sao chép văn bản vào clipboard!")

    tk.Button(view_frame, text="Sao chép văn bản", command=copy_text).pack(pady=10)