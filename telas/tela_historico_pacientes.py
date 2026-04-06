import customtkinter as ctk
from utils.json_manager import listar_atendimentos
from datetime import datetime 


COR_ROXO = "#7c3aed"
COR_BRANCO ="#ffffff"
COR_CINZA = "#6b7280"
COR_CINZA_ESCURO = "#111827"


class HistoricoPacientes(ctk.CTkFrame):

    def __init__(self, master, paciente, voltar_atendimentos):
        super().__init__(master, fg_color=COR_BRANCO)

        self.paciente = paciente
        self.voltar_atendimentos = voltar_atendimentos

        # frame principal
        self.frame_principal = ctk.CTkFrame(self, fg_color=COR_BRANCO)
        self.frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

        # frame header
        self.frame_header = ctk.CTkFrame(self.frame_principal, fg_color=COR_BRANCO)
        self.frame_header.pack(fill="x", pady=(0,20))

        # botão voltar
        self.botao_voltar = ctk.CTkButton(
            self.frame_header,
            text="← Voltar",
            fg_color=COR_ROXO,
            command=self.voltar_atendimentos
        )
        self.botao_voltar.pack(side="left")

        # titulo
        self.label_titulo = ctk.CTkLabel(
            self.frame_principal,
            text=f"Histórico de Atendimentos - {self.paciente['nome']}",
            font=("Arial", 24, "bold"),
            text_color=COR_CINZA_ESCURO
        )
        self.label_titulo.pack(anchor="w", pady=(0,20))

        # frame lista
        self.frame_lista = ctk.CTkScrollableFrame(self.frame_principal, fg_color=COR_BRANCO)
        self.frame_lista.pack(fill="both", expand=True)

        self.carregar_historico()

    def carregar_historico(self):
        self.atendimentos = listar_atendimentos()
        for atendimento in self.atendimentos:
            if int(atendimento["paciente_id"]) == int(self.paciente["id"]):
                self.criar_item(atendimento)
    def criar_item(self, atendimento):

        self.item = ctk.CTkFrame(self.frame_lista, fg_color="#f9fafb", corner_radius=10, border_width=1)
        self.item.pack(fill="x", pady=5)

        # tipo atendimento
        self.label_tipo = ctk.CTkLabel(
            self.item,
            text=atendimento["tipo"],
            font=("Arial",14,"bold"),
            text_color=COR_CINZA_ESCURO
        )
        self.label_tipo.pack(anchor="w", padx=10, pady=(10,0))

        # data
        self.label_data = ctk.CTkLabel(
            self.item,
            text=atendimento["data"],
            text_color=COR_CINZA
        )
        self.label_data.pack(anchor="w", padx=10)

        # status
        self.label_status = ctk.CTkLabel(
            self.item,
            text=f"Status: {atendimento['status']}",
            text_color=COR_CINZA
        )
        self.label_status.pack(anchor="w", padx=10, pady=(0,10))
        self.item.bind("<Enter>", lambda e: self.item.configure(fg_color="#f3f4f6"))
        self.item.bind("<Leave>", lambda e: self.item.configure(fg_color="#f9fafb"))