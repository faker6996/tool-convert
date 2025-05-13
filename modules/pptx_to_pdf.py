from tkinter import filedialog, messagebox
import os
import comtypes.client

def convert_pptx_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PowerPoint files", "*.pptx, *.ppt")])
    if not file_path:
        return

    try:
        default_name = os.path.splitext(os.path.basename(file_path))[0] + ".pdf"
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=default_name)

        if save_path:
            powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
            powerpoint.Visible = 1

            presentation = powerpoint.Presentations.Open(file_path, WithWindow=False)
            presentation.SaveAs(save_path, 32)  # 32 = PDF
            presentation.Close()
            powerpoint.Quit()

            messagebox.showinfo("Thành công", f"Đã chuyển PowerPoint sang PDF: {save_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
