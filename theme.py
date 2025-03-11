class Theme:
    def __init__(self, theme_button, dark_button, frame, theme_frame):
        self.theme_button = theme_button
        self.dark_button = dark_button
        self.frame = frame
        self.theme_frame = theme_frame

    def autumn(self):
        self.theme_button.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.dark_button.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.frame.configure(
            fg_color=["#E1C9B7", "#3F2F25"],
            border_color=["#A6806F", "#6D3F28"],
        )
        self.theme_frame.configure(fg_color=["#F5E5E1", "#3B2F2A"])

    def breeze(self):
        self.theme_button.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.dark_button.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.frame.configure(
            fg_color=["#B4D9E7", "#1E3A46"],
            border_color=["#8AA1AE", "#2C4B5A"],
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])

    def carrot(self):
        self.theme_button.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.dark_button.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.frame.configure(
            fg_color=["#FFC5A1", "#D95136"],
            border_color=["#C7745B", "#8C1C00"],
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])

    def cherry(self):
        self.theme_button.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.dark_button.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.frame.configure(
            fg_color=["#FFF1EA", "#5D3A4A"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.theme_frame.configure(fg_color=["#FBE8E6", "#6D4C6C"])

    def coffee(self):
        self.theme_button.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.dark_button.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.frame.configure(
            fg_color=["#D8C0A0", "#725B4E"],
            border_color=["#A3886F", "#8B746A"],
        )
        self.theme_frame.configure(fg_color=["#E8D1B3", "#6D5143"])

    def lavender(self):
        self.theme_button.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.dark_button.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.frame.configure(
            fg_color=["#9370DB", "#B19CD9"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])

    def marsh(self):
        self.theme_button.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.dark_button.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.frame.configure(
            fg_color=["#B0C9A0", "#4F5F4A"],
            border_color=["#8A9E72", "gray28"],
        )
        self.theme_frame.configure(fg_color=["#B0C9A0", "gray14"])

    def metal(self):
        self.theme_button.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
        self.dark_button.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
        self.frame.configure(
            fg_color=["#C0C0C0", "#404040"],
            border_color=["#808080", "#606060"],
        )
        self.theme_frame.configure(fg_color=["#E0E0E0", "#363636"])
