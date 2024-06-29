import customtkinter
import tkinter
from tkinterdnd2 import TkinterDnD, DND_FILES
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

class CTk(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

class DirectoryPathFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="保存先ディレクトリ")
        self.label.grid(row=0, column=0, padx=10, pady=(10, 0))

        self.text_box = customtkinter.CTkEntry(self, placeholder_text="保存先ディレクトリを選択してください", width=350)
        self.text_box.grid(row=1, column=0, padx=10, pady=(10, 0))

        self.button_select = customtkinter.CTkButton(self, text="ディレクトリを選択...", command=self.select_dir_path)
        self.button_select.grid(row=1, column=1, padx=10, pady=(10, 0))

    def select_dir_path(self):
        dir_path = tkinter.filedialog.askdirectory()
        if dir_path is not None:
            self.text_box.delete(0, tkinter.END)
            self.text_box.insert(0, dir_path)

    def get_dir_path(self):
        return self.text_box.get()

class DrugAndDropFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, width=350, height=250, text="画像をドラッグ&ドロップ", corner_radius=3)
        self.label.grid(row=0, column=0, padx=10, pady=(10, 10))

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("600x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.dir_path_frame = DirectoryPathFrame(self, width=580, height=130)
        self.dir_path_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.drug_and_drop_frame = DrugAndDropFrame(self, width=580, height=230)
        self.drug_and_drop_frame.drop_target_register(DND_FILES)
        self.drug_and_drop_frame.dnd_bind('<<Drop>>', self.get_path)
        self.drug_and_drop_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew")

    def get_path(self, event):
        dropped_file_paths = event.data.replace("{","").replace("}", "").split()
        save_dir_path = self.dir_path_frame.get_dir_path() or ""

        if save_dir_path:
            self.output_pdf(dropped_file_paths, save_dir_path)
        else:
            print("save_dir_path is empty")

    def output_pdf(self, dropped_file_paths, save_dir_path):
        file_name = "HelloWorld.pdf"
        save_file_path = save_dir_path + "/" + file_name
        pdf_canvas = canvas.Canvas(save_file_path, pagesize=portrait(A3))
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
        font_size = 20
        pdf_canvas.setFont('HeiseiMin-W3', font_size)

        for dir_path in dropped_file_paths:
            width, height = A3  # A4用紙のサイズ
            pdf_canvas.drawCentredString(width / 2, height / 2 - font_size * 0.4, dir_path)
            pdf_canvas.showPage()

        print(save_dir_path)
        pdf_canvas.save()

app = App()
app.mainloop()
