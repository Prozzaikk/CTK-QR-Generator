import customtkinter as CTk
from make_qr import make_qr
from PIL import Image
import qr_frame




class App(CTk.CTk):
    def __init__(self):
        super().__init__()


        #Window configuration
        self.geometry("645x590")
        self.resizable(False, False)
        self.title("CTk QR Generator")
        #self.iconbitmap("qr_icon.ico")
        # self.wm_iconbitmap()
        # icopath = ImageTk.PhotoImage(file="qr_icon.ico")
        # self.iconphoto(False, icopath)


        #QR Frame
        self.qr_frame = qr_frame.QrFrame(master=self)
        self.qr_frame.grid(row=0, columnspan=4, pady=10)


        #Reload button
        self.reload_icon_url = "reload.png"
        self.reload_icon = CTk.CTkImage(dark_image=Image.open(self.reload_icon_url), size=(20, 20))
        self.reload_logo_button = CTk.CTkButton(master=self, text="", width=30, height=30,
                                                command=self.reload_logo_button_func, image=self.reload_icon,
                                                fg_color="#43454a", hover_color="#528bff")
        self.reload_logo_button.grid(row=0, column=2, sticky="nw", padx=[50, 0], pady=[10, 0])


        #Entry data for encoding
        self.enter_data_label = CTk.CTkLabel(master=self, text="Enter data for encoding\n"
                                                               " or enter the sequence\n"
                                                               "start to end with -")
        self.enter_data_label.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")
        self.entry_data = CTk.CTkEntry(master=self, width=170)
        self.entry_data.grid(row=1, column=1, sticky="w")


        #Entry file name
        self.enter_filename_label = CTk.CTkLabel(master=self, text="Enter filename")
        self.enter_filename_label.grid(row=2, column=0, padx = (0, 10), pady = 10, sticky="nsew")
        self.entry_filename = CTk.CTkEntry(master=self, width= 170)
        self.entry_filename.grid(row=2, column=1, sticky="w")


        # Pick foreground color for QR code
        self.foreground_qr_color_var = "black"
        self.enter_foreground_color_label = CTk.CTkLabel(master=self, text="Foreground color for QR")
        self.enter_foreground_color_label.grid(row=2, column=2, padx=(30, 15))
        self.foreground_qr_color_option_menu = CTk.CTkOptionMenu(master=self, values=["black", "red", "orange",
                                                                                      "yellow", "green", "blue",
                                                                                      "dark blue", "purple"],
                                                                 command=self.foreground_qr_color_option_menu_callback,
                                                                 width=40,
                                                                 fg_color="#528bff", button_color="#3373f5",
                                                                 button_hover_color="#636d83")
        self.foreground_qr_color_option_menu.grid(row=2, column=3, sticky="w")


        #Entry path to save
        self.enter_path_label = CTk.CTkLabel(master=self, text="Enter path to save QR(-s)")
        self.enter_path_label.grid(row = 3, column = 0, padx = (0, 10), pady = 10, sticky="nsew")
        self.entry_path = CTk.CTkEntry(master=self, width = 170)
        self.entry_path.grid(row = 3, column = 1, sticky="w")


        # Pick background color for QR code
        self.background_qr_color_var = "white"
        self.enter_background_color_label = CTk.CTkLabel(master=self, text="Background color for QR")
        self.enter_background_color_label.grid(row=3, column=2, padx=(30, 15))
        self.background_qr_color_option_menu = CTk.CTkOptionMenu(master=self, values=["white", "red", "orange",
                                                                                      "yellow", "green", "blue",
                                                                                      "dark blue", "purple"],
                                                                 command=self.background_qr_color_option_menu_callback,
                                                                 width=40,
                                                                 fg_color="#528bff", button_color="#3373f5",
                                                                 button_hover_color="#636d83")
        self.background_qr_color_option_menu.grid(row=3, column=3, sticky="w")


        #Entry name and extention for QR file
        self.extention_type_option_menu_var = ".png"
        self.enter_extention_type_label = CTk.CTkLabel(master=self, text="Choose extension type\n"
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
        self.generate_qr_btn.grid(row = 6, columnspan=4, pady=(10, 5))

        self.develop_by = CTk.CTkLabel(master=self, text="Designed & Develop by prozzaikk (Fyodor Borichev)",
                                       text_color="#494d57")
        self.develop_by.grid(row=7, columnspan=4, sticky="nsew")

        self.error_image_arr = [".\\input_data_error.png", "./input_data_error.png", ".\\sequence_input_error.png",
                                "./sequence_input_error.png"]

    def reload_logo_button_func(self):
        self.qr_frame.show_generated_qr(new_qr_image_url="qr_icon.png")


    #Method for showing generated qr code
    def switch_is_show(self):
        self.is_show_true = int(self.switch_show_var.get())
        return self.is_show_true


    #method for generating qr code and updating the logo or for displaying the generated qr code
    def generate_qr_btn(self):
        new_qr_image_url = make_qr(data_to_qr=self.entry_data.get(), filename=self.entry_filename.get(),
                                   path_to_save=self.entry_path.get(), qr_type=self.extention_type_option_menu_var,
                                   foreground_color=self.foreground_qr_color_var, background_color=self.background_qr_color_var)
        if self.is_show_true or new_qr_image_url in self.error_image_arr:
            self.qr_frame.show_generated_qr(new_qr_image_url=new_qr_image_url)


    def extention_type_option_menu_callback(self, choice):
        self.extention_type_option_menu_var = choice
        return self.extention_type_option_menu


    def foreground_qr_color_option_menu_callback(self,choice):
        self.foreground_qr_color_var = choice
        return self.foreground_qr_color_option_menu


    def background_qr_color_option_menu_callback(self,choice):
        self.background_qr_color_var = choice
        return self.background_qr_color_option_menu




if __name__ == "__main__":
    app = App()
    app.mainloop()
