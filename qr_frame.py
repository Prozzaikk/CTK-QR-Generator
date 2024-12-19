import customtkinter as CTk
from PIL import Image


class QrFrame(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.qr_image_url = ".\\qr_icon.png"
        self.qr_image = CTk.CTkImage(dark_image=Image.open(self.qr_image_url), size=(200, 200))
        self.qr_image_label = CTk.CTkLabel(master=self, text="", image=self.qr_image)
        self.qr_image_label.grid(row=0, column=0, sticky="nsew")


    def show_generated_qr(self, new_qr_image_url):
        self.qr_image_url = new_qr_image_url
        self.qr_image = CTk.CTkImage(dark_image=Image.open(self.qr_image_url), size=(200, 200))
        self.qr_image_label = CTk.CTkLabel(master=self, text="", image=self.qr_image)
        self.qr_image_label.grid(row=0, column=0)
