from tkinter import filedialog, messagebox
from PIL import Image
import os

def convert_image_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if not file_path:
        return

    try:
        img = Image.open(file_path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        default_name = os.path.splitext(os.path.basename(file_path))[0] + ".pdf"
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=default_name)
        if save_path:
            img.save(save_path, "PDF", resolution=100.0)
            messagebox.showinfo("Thành công", f"Đã lưu file: {save_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
