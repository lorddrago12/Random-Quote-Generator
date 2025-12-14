import customtkinter as ctk
import random
from tkinter import messagebox
# Set up  the dark mode appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class QuoteGeneratorApp(ctk.CTk):

    # -- 1. static lists of quotes -- 
    quotes = [
        'The only way to do great work is to love what you do. - steve jobs',
        'Life is what happens when you\'re busy making other plans. - john lennon',
        'Get busy living or get busy dying. - stephen king',
        'You have within you right now, everything you need to deal with whatever the world can throw at you. - brian tracy',
        'Believe you can and you\'re halfway there. - theodore roosevelt',  
        'The purpose of our lives is to be happy. - dalai lama',
        'The best way to predict the future is to invent it. - alan kay'
    ]

    def __init__(self):
        super().__init__()

        #main window configuration
        self.title("Random Quote Generator")
        self.geometry("650x400") # slightly increased size for the new button

        # current quote storage
        self.current_quote = self.quotes[0]

        self.quote_label = ctk.CTkLabel(
            self,
            text=self.current_quote,
            wraplength=500,
            font=("Arial", 16),
            justify="center"
        )
        self.quote_label.pack(pady=40)

        self.generate_button = ctk.CTkButton(
            self,
            text="Generate Quote",
            command=self.generate_quote
        )
        self.generate_button.pack(pady=20)

    def generate_quote(self):
        self.current_quote = random.choice(self.quotes)
        self.quote_label.configure(text=self.current_quote)


if __name__ == "__main__":
    app = QuoteGeneratorApp()
    app.mainloop()
