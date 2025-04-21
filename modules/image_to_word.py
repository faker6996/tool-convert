from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
from docx import Document
import os

def convert_image_to_word():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if not file_path:
        return

    try:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

        doc = Document()
        doc.add_paragraph(text)

        default_name = os.path.splitext(os.path.basename(file_path))[0] + ".docx"
        save_path = filedialog.asksaveasfilename(defaultextension=".docx", initialfile=default_name)
        if save_path:
            doc.save(save_path)
            messagebox.showinfo("Thành công", f"Đã lưu file: {save_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
