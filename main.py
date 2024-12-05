from lib2to3.patcomp import tokenize_wrapper

import customtkinter as CTk
from make_qr import make_qr
# from qr_frame import QR_Frame
from PIL import Image

class App(CTk.CTk):
    def __init__(self):
        super().__init__()


        #Window configuration
        self.geometry("370x575")
        self.resizable(False, False)
        self.title("CTk QR Generator")
        self.iconbitmap("qr_icon.ico")


        #QR Frame
        self.qr_image_url = ".\\qr_icon.png"
        self.qr_image = CTk.CTkImage(dark_image=Image.open(self.qr_image_url), size=(200, 200))
        self.qr_image_label = CTk.CTkLabel(master=self, text="", image=self.qr_image)
        self.qr_image_label.grid(row=0, columnspan=2, pady=10)


        #Entry data for encoding
        self.enter_data_label = CTk.CTkLabel(master=self, text="Enter data for encoding or\n"
                                                               "Enter the sequence from\n"
                                                               "start to end with -")
        self.enter_data_label.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")
        self.entry_data = CTk.CTkEntry(master=self, width=170)
        self.entry_data.grid(row=1, column=1, sticky="w")


        #Entry file name
        self.enter_filename_label = CTk.CTkLabel(master=self, text="Enter filename")
        self.enter_filename_label.grid(row=2, column=0, padx = (0, 10), pady = 10, sticky="nsew")
        self.entry_filename = CTk.CTkEntry(master=self, width= 170)
        self.entry_filename.grid(row=2, column=1, sticky="w")


        #Entry path to save
        self.enter_path_label = CTk.CTkLabel(master=self, text="Enter path to save QR(-s)")
        self.enter_path_label.grid(row = 3, column = 0, padx = (0, 10), pady = 10, sticky="nsew")
        self.entry_path = CTk.CTkEntry(master=self, width = 170)
        self.entry_path.grid(row = 3, column = 1, sticky="w")


        #Entry name and extention for QR file
        self.extention_type_option_menu_var = ".png"
        self.enter_extention_type_label = CTk.CTkLabel(master=self, text="Choose extention type\n"
                                                                    "for QR(-s) (.png, .pdf, .svg)")
        self.enter_extention_type_label.grid(row = 4, column = 0, padx = (0, 10), pady = 10, sticky="nsew")
        self.extention_type_option_menu = CTk.CTkOptionMenu(master=self, values=[".png", ".pdf", ".svg"],
                                                            command=self.extention_type_option_menu_callback, width=40,
                                                            fg_color="#528bff", button_color="#3373f5",
                                                            button_hover_color="#636d83")
        self.extention_type_option_menu.grid(row = 4, column = 1, sticky="w")


        #Show QR after encoding
        self.show_switch_label = CTk.CTkLabel(master=self, text="Show QR after encoding data\n"
                                                                "(when generating a sequence,\n"
                                                                "it outputs the last qr)")
        self.show_switch_label.grid(row = 5, column = 0, padx = (10, 10), pady = 10, sticky="nsew")
        self.switch_show_var = CTk.StringVar(value="0")
        self.show_qr_switch = CTk.CTkSwitch(master=self, text="", variable=self.switch_show_var, onvalue="1",
                                            offvalue="0", command=self.switch_is_show, progress_color="#528bff")
        self.show_qr_switch.grid(row = 5, column = 1, sticky="nsew")
        self.is_show_true = 0


        #Generate QR button
        self.generate_qr_btn = CTk.CTkButton(master=self, text="Generate QR code", width=150,
                                             command=self.generate_qr_btn, fg_color="#528bff", hover_color="#636d83")
        self.generate_qr_btn.grid(row = 6, columnspan=2, pady=(10, 5))

        self.develop_by = CTk.CTkLabel(master=self, text="Designed & Develop by prozzaikk (Fyodor Borichev)",
                                       text_color="#494d57")
        self.develop_by.grid(row=7, columnspan=2)

    def switch_is_show(self):
        self.is_show_true = int(self.switch_show_var.get())
        return self.is_show_true


    def generate_qr_btn(self):
        new_qr_image_url = make_qr(data_to_qr=self.entry_data.get(), filename=self.entry_filename.get(),
                                   path_to_save=self.entry_path.get(), qr_type=self.extention_type_option_menu_var)
        if self.is_show_true:
            self.qr_image_url = new_qr_image_url
            self.qr_image = CTk.CTkImage(dark_image=Image.open(self.qr_image_url), size=(200, 200))
            self.qr_image_label = CTk.CTkLabel(master=self, text="", image=self.qr_image)
            self.qr_image_label.grid(row=0, columnspan=2, pady=10)


    def extention_type_option_menu_callback(self, choice):
        self.extention_type_option_menu_var = choice
        return self.extention_type_option_menu




if __name__ == "__main__":
    app = App()
    app.mainloop()