import customtkinter as ctk
from tkinter import PhotoImage

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
FRAME_WIDTH = 490
FRAME_HEIGHT = 590
ICON_PATH = "../../img/icon.ico"
LOGIN_IMG_PATH = "../../img/login.png"

class LoginApp:
    
    def __init__(self):
        self.window = self._create_window()
        self._create_login_frame()
        self.window.mainloop()

    def _create_window(self):
        window = ctk.CTk()
        window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        window.title("Tela de Login")
        window.iconbitmap(ICON_PATH)
        window.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        return window

    def _create_login_frame(self):
        self.frame_login = ctk.CTkFrame(
            master=self.window, width=FRAME_WIDTH, height=FRAME_HEIGHT
        )
        self.frame_login.pack(side="right")
        
        self._add_login_elements()
    
    def _add_login_elements(self):

        self._add_login_image()
        self._add_login_labels_entries()
        self._add_login_buttons()

    def _add_login_image(self):
        img_login = PhotoImage(file=LOGIN_IMG_PATH)
        ctk.CTkLabel(
            master=self.window, image=img_login, text=None
        ).place(x=10, y=75)

    def _add_login_labels_entries(self):
        ctk.CTkLabel(
            master=self.frame_login,
            text="Faça seu Login",
            font=('Roboto', 40, 'bold'),
            text_color='white',
            justify="center"
        ).place(x=110, y=140)

        self.user_entry = self._create_entry(
            self.frame_login, 
            "Digite Seu login", 
            230
        )
        self._create_message_label(
            self.frame_login, 
            "*O Nome do Usuario é Obrigatorio", 
            265
        )

        self.pass_entry = self._create_entry(
            self.frame_login,
            "Digite Sua Senha", 
            305, 
            show="*"
        )
        
        self._create_message_label(
            self.frame_login,
            "*A Senha do Usuario é Obrigatorio", 
            345
        )

        ctk.CTkCheckBox(
            master=self.frame_login,
            text="Salvar este Usuario"
        ).place(x=40, y=385)

    def _add_login_buttons(self):
        ctk.CTkButton(
            master=self.frame_login,
            text="LOGIN",
            width=300,
            height=40
        ).place(x=110, y=425)

        ctk.CTkLabel(
            master=self.frame_login,
            text="Não possui uma conta?",
            font=('Roboto', 13)
        ).place(x=113, y=470)

        ctk.CTkButton(
            master=self.frame_login,
            text="CADASTRE-SE",
            width=150,
            fg_color="green",
            hover_color="#2D9334",
            command=self._show_register_frame
        ).place(x=260, y=470)

    def _create_entry(self, master, placeholder, y, show=None):
        return ctk.CTkEntry(
            master=master,
            placeholder_text=placeholder,
            width=420,
            font=('Roboto', 20),
            show=show
        ).place(x=40, y=y)

    def _create_message_label(self, master, text, y):
        ctk.CTkLabel(
            master=master,
            text=text,
            text_color="#00B0F0",
            font=('Roboto', 15)
        ).place(x=40, y=y)

    def _show_register_frame(self):
        self.frame_login.pack_forget()
        self.frame_register = self._create_register_frame()
        self._add_register_elements()

    def _create_register_frame(self):
        frame_register = ctk.CTkFrame(
            master=self.window, width=FRAME_WIDTH, height=FRAME_HEIGHT
        )
        frame_register.pack(side="right")
        return frame_register

    def _add_register_elements(self):
        ctk.CTkLabel(
            master=self.frame_register,
            text="Faça seu Cadastro",
            font=('Roboto', 40, 'bold'),
            text_color='white',
            justify="center"
        ).place(x=85, y=70)

        self._create_entry(self.frame_register, "Digite Seu Nome", 140)
        self._create_message_label(self.frame_register, "*O Nome do Usuario é Obrigatorio", 170)

        self._create_entry(self.frame_register, "Digite Seu Email", 210)
        self._create_message_label(self.frame_register, "*O Email do Usuario é Obrigatorio", 240)

        self._create_entry(self.frame_register, "Digite Sua Função na Empresa", 280)
        self._create_message_label(self.frame_register, "*A Função do Usuario é Obrigatorio", 320)

        self._create_entry(self.frame_register, "Digite Sua Senha", 360, show="*")
        self._create_message_label(self.frame_register, "*A Senha do Usuario é Obrigatorio", 400)

        ctk.CTkCheckBox(
            master=self.frame_register,
            text="Aceita todos os Termos e Políticas?"
        ).place(x=40, y=440)

        ctk.CTkButton(
            master=self.frame_register,
            text="CADASTRE-SE",
            width=300,
            height=40,
            fg_color="green",
            hover_color="#2D9334"
        ).place(x=110, y=480)

        ctk.CTkButton(
            master=self.frame_register,
            text="VOLTAR",
            width=300,
            height=40,
            fg_color="red",
            hover_color="#9F0101",
            command=self._back_to_login
        ).place(x=110, y=530)

    def _back_to_login(self):
        """Retorna ao frame de login a partir do frame de registro."""
        self.frame_register.pack_forget()
        self.frame_login.pack(side="right")

if __name__ == "__main__":
    LoginApp()
