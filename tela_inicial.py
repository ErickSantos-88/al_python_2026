("Samuel e Erick")

import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Credenciais de acesso pré-definidas
usuario_admin = Usuario("admin", "123")

class AppSGU(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gerenciamento de Usuários (SGU)")
        self.geometry("400x300")
        self.tela_atual = None
        self.mostrar_tela_login()

    def mostrar_tela_login(self):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaLogin(self, self.fazer_login)

    def mostrar_tela_menu(
