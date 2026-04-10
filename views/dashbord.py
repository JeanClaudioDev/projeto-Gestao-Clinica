import customtkinter as ctk
from tkinter import ttk
from services.json_manager import convert_date_for_label
from controllers.atendimento_controller import listar_atendimentos
from controllers.paciente_controller import listar_pacientes
from datetime import datetime
from pathlib import Path
from PIL import Image

"""| Cor | Código | Uso |"""

COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#90b7f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA_CLARO = "#f9fafb" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

"""Cores dos Status na Tabela:
Status | Cor de Fundo | Cor do Texto |"""

FUNDO_REALIZADO = "#dcfce7" #verde claro fundo
TEXTO_REALIZADO = "#166534" #verde escuro texto

FUNDO_ACOMPANHAMENTO = "#dbeafe" #azul claro fundo
TEXTO_ACOMPANHAMENTO = "#1e40af" #azul escuro texto

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_IMG_MASK = BASE_DIR / "assets" / "mask.png"
PATH_IMG_TOTAl = BASE_DIR / "assets" / "quality-service.png"
PATH_IMG_TODAY = BASE_DIR / "assets" / "calendar.png"

class Dashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_CINZA_CLARO)
        self.frame_titulo = ctk.CTkFrame(self, fg_color=COR_CINZA_CLARO)
        self.frame_titulo.pack(padx=20,pady=(50,5),anchor='w')

        self.label_bem_vindo = ctk.CTkLabel(
            self.frame_titulo,
            text="Bem-vindo(a) de volta! 👋",
            text_color=COR_ROXO,
            font=("Arial", 20, "bold")
        )
        self.label_bem_vindo.pack(pady=5, anchor='w')

        self.titulo = ctk.CTkLabel(
            self.frame_titulo,
            text="Dashboard",
            text_color=COR_CINZA_ESCURO,
            font=("Arial", 28, "bold")
        )
        self.titulo.pack(pady=5, anchor='w')
        self.label_data = ctk.CTkLabel(self.frame_titulo,
                                       text=convert_date_for_label(),
                                       text_color=COR_CINZA_ESCURO,font=("Arial", 20, "bold"))
        self.label_data.pack(pady=5, anchor='w')
        #frame para os cards
        self.frame_cards = ctk.CTkFrame(self, fg_color=COR_CINZA_CLARO)
        self.frame_cards.pack(pady=(5,20), padx=20,fill='both', expand=True)
        self.frame_cards.grid_columnconfigure(0, weight=2)
        self.frame_cards.grid_columnconfigure(1, weight=2)
        self.frame_cards.grid_columnconfigure(2, weight=2)
        self.frame_cards.grid_rowconfigure(0,weight=1)

        mask = ctk.CTkImage(light_image=Image.open(PATH_IMG_MASK),
                                  dark_image=Image.open(PATH_IMG_MASK),
                                  size=(30, 30))
        
        #frame para o card total pacientes
        self.frame_total_pacientes, self.label_numero_pacientes = self.criar_card_dashboard(mask,"Total de Pacientes")
        self.frame_total_pacientes.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

        total = ctk.CTkImage(light_image=Image.open(PATH_IMG_TOTAl),
                                  dark_image=Image.open(PATH_IMG_TOTAl),
                                  size=(30, 30))
        #frame para atendimentos registrado
        self.frame_atendimentos, self.numero_atendimentos = self.criar_card_dashboard(total,"Atendimentos Registrados")
        hoje = ctk.CTkImage(light_image=Image.open(PATH_IMG_TODAY),
                                  dark_image=Image.open(PATH_IMG_TODAY),
                                  size=(30, 30))
        self.frame_atendimentos.grid(row=0, column=1, pady=20, padx=20, sticky="ew")
        #frame atendimentos hoje
        self.frame_atendimentos_hoje, self.numero_atendimentos_hoje = self.criar_card_dashboard(hoje,"Atendimentos Hoje")
        self.frame_atendimentos_hoje.grid(row=0, column=2, pady=20, padx=20, sticky="ew")
        
        #frame tabela
        self.frame_tabela = ctk.CTkFrame(self, fg_color=COR_BRANCO,
                                         corner_radius=20)
        self.frame_tabela.pack(pady=20, padx=20,fill='x')
        #label tabela titulo
        self.label_titulo_tabela = ctk.CTkLabel(self.frame_tabela,
                                                text="Atendimentos de Hoje",
                                                text_color=COR_CINZA_ESCURO,
                                                font=("Arial", 16, "bold"))
        self.label_titulo_tabela.pack(pady=30, padx=30, anchor="w")
        #estilo treeview
        style = ttk.Style()
        style.configure("Treeview",rowheight=35,font=("Arial", 13),background=COR_BRANCO,fieldbackground=COR_BRANCO)

        style.configure("Treeview.Heading",
                        font=("Arial", 13, "bold"))
        #treeviw tabela
        self.tabela = ttk.Treeview(self.frame_tabela,
                                   columns=("Paciente",
                                            "Data",
                                            "Tipo",
                                            "Status"),
                                            show="headings",)
        self.tabela.pack(fill="both", expand=True, padx=20, pady=10)
        #adicionando na tabela
        self.tabela.heading("Paciente", text="Paciente", anchor='w')
        self.tabela.heading("Data", text="Data", anchor='w')
        self.tabela.heading("Tipo", text="Tipo", anchor='w')
        self.tabela.heading("Status", text="Status", anchor='w')
        #largura das colunas
        self.tabela.column("Paciente", width=220, anchor='w')
        self.tabela.column("Data", width=100, anchor='w')
        self.tabela.column("Tipo", width=150, anchor='w')
        self.tabela.column("Status", width=130, anchor="w")
        self.tabela.tag_configure("realizado",background=FUNDO_REALIZADO,foreground=TEXTO_REALIZADO)
        self.tabela.tag_configure("acompanhamento",background=FUNDO_ACOMPANHAMENTO,foreground=TEXTO_ACOMPANHAMENTO)
        self.atualizar_dashboard()
        self.carregar_atendimentos_hoje()
    def criar_card_dashboard(self, emoji, titulo):
        card = ctk.CTkFrame(self.frame_cards, fg_color=COR_AZUL, corner_radius=20)
        card.bind("<Enter>", lambda e: card.configure(border_color=COR_BRANCO))
        card.bind("<Leave>", lambda e: card.configure(border_color="#e5e7eb"))
        card.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(card, image=emoji,text='')

        label.grid(row=0, column=0,pady=15,padx=15,sticky='w')
        label_titulo = ctk.CTkLabel(card,text=titulo,
                                    text_color=COR_CINZA_ESCURO,
                                    font=("Arial", 20, "bold"))
        label_titulo.grid(row=1, column=0,pady=15,padx=15, sticky='w')
        label_numero = ctk.CTkLabel(card,text="0",
                                    text_color=COR_CINZA_ESCURO,
                                    font=("Arial", 40, "bold"))
        label_numero.grid(row=2,column=0,pady=15,padx=15, sticky='w')
        return card, label_numero
    def carregar_atendimentos_hoje(self):

        for i in self.tabela.get_children():
            self.tabela.delete(i)

        atendimentos = listar_atendimentos()
        pacientes = listar_pacientes()

        pacientes_dict = {p["id"]: p["nome"] for p in pacientes}
        hoje = datetime.now().strftime("%d/%m/%Y")

        for atendimento in atendimentos:
            if atendimento["data"]!= hoje:
                continue
            nome_paciente = pacientes_dict.get(
                atendimento["paciente_id"], "Desconhecido")

            status = atendimento["status"]
            tag = ""
            if status == "Realizado":
                tag = "realizado"
            elif status == "Em Acompanhamento":
                tag = "acompanhamento"
            self.tabela.insert(
                "",
                "end",
                values=(
                    nome_paciente,
                    atendimento["data"],
                    atendimento["tipo"],
                    atendimento["status"]),tags=(tag,))
    def atualizar_dashboard(self):
        pacientes = listar_pacientes()
        atendimentos = listar_atendimentos()
        total_pacientes = len(pacientes)
        total_atendimentos = len(atendimentos)
        hoje = datetime.now().strftime("%d/%m/%Y")
        atendimentos_hoje = 0
        for atendimento in atendimentos:
            if atendimento["data"] == hoje:
                atendimentos_hoje += 1
        self.label_numero_pacientes.configure(text=str(total_pacientes))
        self.numero_atendimentos.configure(text=str(total_atendimentos))
        self.numero_atendimentos_hoje.configure(text=str(atendimentos_hoje))