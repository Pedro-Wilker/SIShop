import customtkinter as ctk
import database
from tkinter import *

window = ctk.CTk()

frame_config = ctk.CTkFrame(
    master=window, 
    width=490, 
    height=590
)
frame_config.pack(side=RIGHT)
frame_login = frame_config


class Login():
    
    def __init__(self):
        self.window = window
        self.theme()
        self.screen()
        self.screen_login()
        self.img_login()
        window.mainloop()
        
    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def screen(self):
        window.geometry("900x600")
        window.title("Tela de Login")
        window.iconbitmap("../../img/icon.ico")
        window.resizable(False, False)
        
    def img_login(self):
        img_login = PhotoImage(file="../../img/login.png")
        
        label_img = ctk.CTkLabel(
            master=window, 
            image=img_login, 
            text=None
        ).place(x=10, y=75)
  

    def screen_login(self):                   
        label_login = ctk.CTkLabel(
            master=frame_login,
            text="Faça seu Login", 
            font = ('Roboto', 40, 'bold'), 
            text_color= ('white'), 
            justify="center"
            
        ).place(x=110, y=140)

        entry_user = ctk.CTkEntry(
            master=frame_login, 
            placeholder_text="Digite Seu login", 
            width=420, 
            font=('Roboto', 20)
        ).place(x=40,y=230)
        
        msg_user= ctk.CTkLabel(
            master=frame_login, 
            text="*O Nome do Usuario é Obrigatorio", 
            text_color="#00B0F0", 
            font=('Roboto',15)
        ).place(x=40,y=265)
        
        entry_pass = ctk.CTkEntry(
            master=frame_login, 
            placeholder_text="Digite Sua Senha", 
            width=420, 
            font=('Roboto', 20), show="*"
        ).place(x=40,y=305)
        
        msg_pass= ctk.CTkLabel(
            master=frame_login, 
            text="*A Senha do Usuario é Obrigatorio", 
            text_color="#00B0F0", 
            font=('Roboto',15)
        ).place(x=40,y=345)

        checkbox = ctk.CTkCheckBox(
            master=frame_login,
            text="Salvar este Usuario"
        ).place(x=40,y=385)
        
        btn_login = ctk.CTkButton(
            master=frame_login, 
            text="LOGIN", 
            width=300,
            height=40
        ).place(x=110, y=425)
    
        label_rgt = ctk.CTkLabel(
            master=frame_login, 
            text="Não possui uma conta?",       
            font=('Roboto', 13)
        ).place(x=113, y=470) 
        
        def screen_register():
            frame_login.pack_forget()
            frame_register = ctk.CTkFrame(
                master=window, 
                width=490, 
                height=590
            )
            frame_register.pack(side=RIGHT)

            label_register = ctk.CTkLabel(
                master=frame_register,
                text="Faça seu Cadastro", 
                font = ('Roboto', 40, 'bold'), 
                text_color= ('white'), 
                justify="center"
            ).place(x=85, y=70)
            
            entry_nome = ctk.CTkEntry(
                master=frame_register, 
                placeholder_text="Digite Seu Nome", 
                width=420, 
                font=('Roboto', 20)
            ).place(x=40,y=140)
        
            msg_nome= ctk.CTkLabel(
                master=frame_register, 
                text="*O Nome do Usuario é Obrigatorio", 
                text_color="#00B0F0", 
                font=('Roboto',15)
            ).place(x=40,y=170)
            
            entry_email = ctk.CTkEntry(
                master=frame_register, 
                placeholder_text="Digite Seu Email", 
                width=420, 
                font=('Roboto', 20)
            ).place(x=40,y=210)
        
            msg_email= ctk.CTkLabel(
                master=frame_register, 
                text="*O Email do Usuario é Obrigatorio", 
                text_color="#00B0F0", 
                font=('Roboto',15)
            ).place(x=40,y=240)
            
            entry_funcao = ctk.CTkEntry(
                master=frame_register, 
                placeholder_text="Digite Sua Função na Empresa",  
                width=420, 
                font=('Roboto', 20)
            ).place(x=40,y=280)
        
            msg_funcao= ctk.CTkLabel(
                master=frame_register, 
                text="*A Função do Usuario é Obrigatorio", 
                text_color="#00B0F0", 
                font=('Roboto',15)
            ).place(x=40,y=320)
            
            entry_passrg = ctk.CTkEntry(
                master=frame_register, 
                placeholder_text="Digite Sua Senha", 
                width=420, 
                font=('Roboto', 20), show="*"
            ).place(x=40,y=360)
            
            msg_passrg= ctk.CTkLabel(
                master=frame_register, 
                text="*A Senha do Usuario é Obrigatorio", 
                text_color="#00B0F0", 
                font=('Roboto',15)
            ).place(x=40,y=400)
            
            checkbox = ctk.CTkCheckBox(
                master=frame_register,
                text="Aceita todos os Termos e Políticas?"
            ).place(x=40,y=440)
            
            btn_rg = ctk.CTkButton(
                master=frame_register,
                text="CADASTRE-SE", 
                width=300,
                height=40,
                fg_color="green", 
                hover_color="#2D9334", 
                command=save_user
            ).place(x=110, y=480 )
            
            def back_lg():
                frame_register.pack_forget()
                frame_login.pack(side=RIGHT)
                
            btn_back = ctk.CTkButton(
                master=frame_register,
                text="VOLTAR", 
                width=300,
                height=40,
                fg_color="red", 
                hover_color="#9F0101", 
                command=back_lg
            ).place(x=110, y=530 )
    
        
        btn_register = ctk.CTkButton(
            master=frame_login,
            text="CADASTRE-SE", 
            width=150, 
            fg_color="green", 
            hover_color="#2D9334", 
            command=screen_register
        ).place(x=260, y=470 )
        
               



Login()