import customtkinter as ctk

from View import View


class MainView(View):
    
    def configure_ui(self):
        self.title("Menu inicial")
        self.theme = "light"
        self._set_appearance_mode("light")

        button = ctk.CTkButton(self, text="Hello World")
        button.pack(pady=20, padx=20)


if __name__ == "__main__":
    view = MainView()
    view.mainloop()
