from tkinter import filedialog, messagebox
from docx2pdf import convert
import os

def convert_word_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if not file_path:
        return

    try:
        output_dir = os.path.dirname(file_path)
        convert(file_path, output_dir)

        pdf_path = os.path.splitext(file_path)[0] + ".pdf"
        if os.path.exists(pdf_path):
            messagebox.showinfo("Thành công", f"Đã chuyển Word sang PDF: {pdf_path}")
        else:
            messagebox.showwarning("Thông báo", "Không tìm thấy file PDF sau khi chuyển.")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
