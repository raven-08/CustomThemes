import customtkinter as ctk
from PIL import Image
from theme import Theme


class SpectrumAnalyzerGUI(ctk.CTkFrame):
    ctk.set_appearance_mode("light")

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.parent = master
        self.is_darked = False
        self.is_theme_open = False

        self.poppins = ctk.CTkFont(family="Poppins")
        self.parent.title("Spectrum Analyzer")
        self.parent.geometry("1000x600")

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame = ctk.CTkFrame(self, corner_radius=10)
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.theme_frame = ctk.CTkFrame(
            self.frame,
            corner_radius=8,
            width=250,
            height=450,
        )

        self.dark_icon = ctk.CTkImage(
            light_image=Image.open("icons/moon.png"),
            dark_image=Image.open("icons/moon_dark.png"),
            size=(20, 20),
        )
        self.sun_icon = ctk.CTkImage(
            light_image=Image.open("icons/sun.png"),
            dark_image=Image.open("icons/sun_dark.png"),
            size=(20, 20),
        )
        self.theme_icon = ctk.CTkImage(
            light_image=Image.open("icons/theme.png"),
            dark_image=Image.open("icons/theme_dark.png"),
            size=(20, 20),
        )

        self.dark_button = ctk.CTkButton(
            self.frame,
            image=self.dark_icon,
            text="",
            text_color="white",
            font=(self.poppins, 14, "bold"),
            height=40,
            width=40,
            corner_radius=4,
            command=self.lightDarkMode,
        )

        self.theme_button = ctk.CTkButton(
            self.frame,
            image=self.theme_icon,
            text="",
            text_color="white",
            font=(self.poppins, 14, "bold"),
            height=40,
            width=40,
            corner_radius=4,
            command=self.toggleThemeFrame,
        )

        self.dark_button.place(relx=0.90, rely=0.05, anchor="ne")
        self.theme_button.place(relx=0.96, rely=0.05, anchor="ne")

        # Theme Buttons
        self.autumn = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            border_color=["#BF8F7C", "#6D4F4D"],
            command=self.setAutumnTheme,
        )
        self.autumn.place(relx=0.2, rely=0.1, anchor="n")
        self.breeze = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            border_color=["#4D7A8D", "#9B9F9F"],
            command=self.setBreezeTheme,
        )
        self.breeze.place(relx=0.4, rely=0.1, anchor="n")
        self.carrot = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setCarrotTheme,
        )
        self.carrot.place(relx=0.6, rely=0.1, anchor="n")
        self.cherry = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            border_color=["#F4A3A0", "#A8A8A8"],
            command=self.setCherryTheme,
        )
        self.cherry.place(relx=0.8, rely=0.1, anchor="n")
        self.coffee = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setCoffeeTheme,
        )
        self.coffee.place(relx=0.8, rely=0.1, anchor="n")
        self.lavender = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setLavenderTheme,
        )
        self.lavender.place(relx=0.2, rely=0.21, anchor="n")
        self.marsh = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setMarshTheme,
        )
        self.marsh.place(relx=0.4, rely=0.21, anchor="n")
        self.theme = Theme(
            self.theme_button, self.dark_button, self.frame, self.theme_frame
        )

    def lightDarkMode(self):
        if self.is_darked:
            ctk.set_appearance_mode("light")
            self.dark_button.configure(image=self.dark_icon)
        else:
            ctk.set_appearance_mode("dark")
            self.dark_button.configure(image=self.sun_icon)

        self.is_darked = not self.is_darked

    def toggleThemeFrame(self):
        if self.is_theme_open:
            self.theme_frame.place_forget()
        else:
            self.theme_frame.place(relx=0.98, rely=0.16, anchor="ne")  # Show the frame

        self.is_theme_open = not self.is_theme_open

    def setAutumnTheme(self):
        self.theme.autumn()

    def setBreezeTheme(self):
        self.theme.breeze()

    def setDefaultTheme(self):
        self.theme.default()

    def setCarrotTheme(self):
        self.theme.carrot()

    def setCherryTheme(self):
        self.theme.cherry()

    def setCoffeeTheme(self):
        self.theme.coffee()

    def setLavenderTheme(self):
        self.theme.lavender()

    def setMarshTheme(self):
        self.theme.marsh()


root = ctk.CTk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = SpectrumAnalyzerGUI(root)
root.mainloop()
