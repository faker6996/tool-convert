from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import os

def convert_image_to_text():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if not file_path:
        return

    try:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

        default_name = os.path.splitext(os.path.basename(file_path))[0] + ".txt"
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name)
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Thành công", f"Đã lưu file: {save_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
