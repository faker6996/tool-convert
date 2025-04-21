from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os

def convert_pdf_to_word():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    try:
        default_name = os.path.splitext(os.path.basename(file_path))[0] + ".docx"
        save_path = filedialog.asksaveasfilename(defaultextension=".docx", initialfile=default_name)

        if save_path:
            cv = Converter(file_path)
            cv.convert(save_path, start=0, end=None)
            cv.close()
            messagebox.showinfo("Thành công", f"Đã chuyển PDF sang Word: {save_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
