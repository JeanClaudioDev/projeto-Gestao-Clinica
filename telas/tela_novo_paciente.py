import customtkinter as ctk
from tkcalendar import DateEntry

COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA = "#808080" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

"""Cores dos Status na Tabela:
Status | Cor de Fundo | Cor do Texto |"""

FUNDO_REALIZADO = "#dcfce7" #verde claro fundo
TEXTO_REALIZADO = "#166534" #verde escuro texto

FUNDO_ACOMPANHAMENTO = "#dbeafe" #azul claro fundo
TEXTO_ACOMPANHAMENTO = "#1e40af" #azul escuro texto

class NovoPaciente(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_ROXO)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #frame titulo
        self.frame_titulo = ctk.CTkFrame(self,
                                         fg_color=COR_ROXO)
        self.frame_titulo.grid(row=0, column=0)
        #labels titulo
        self.emoji_titulo = ctk.CTkLabel(self.frame_titulo,
                                         text="💾",
                                         font=("Arial",50))
        self.emoji_titulo.pack()
        self.label_novo_paciente = ctk.CTkLabel(self.frame_titulo,
                                                   text="Novo Paciente",
                                                   text_color=COR_BRANCO,
                                                   font=("Arial", 24, "bold"))
        self.label_novo_paciente.pack()

        self.label_detalhes_paciente = ctk.CTkLabel(self.frame_titulo,
                                                    text="Registre os detalhes do Paciente",
                                                    text_color=COR_BRANCO,
                                                    font=('Arial', 12, 'bold'))
        self.label_detalhes_paciente.pack()
        #frame principal
        self.frame_principal = ctk.CTkFrame(self, fg_color=COR_BRANCO,
                                            corner_radius=20,
                                            width=400)
        self.frame_principal.grid(row=1, column=0, pady=20, padx=20)
        #card nome completo
        self.card_nome_completo = ctk.CTkFrame(self.frame_principal,
                                               fg_color=COR_BRANCO)
        self.card_nome_completo.pack(fill='x', expand=True, pady=5, padx=20)
        #label nome completo
        self.label_nome_completo = ctk.CTkLabel(self.card_nome_completo,
                                                text="Nome Completo",
                                                text_color=COR_ROXO,
                                                font=("Arial", 12, "bold"))
        self.label_nome_completo.pack(anchor='w')
        #entry nome completo
        self.entry_nome_completo = ctk.CTkEntry(self.card_nome_completo,
                                                placeholder_text="Maria da Silva",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA)
        self.entry_nome_completo.pack(anchor='w')
        #card data de nascimento
        self.card_data_nascimento = ctk.CTkFrame(self.frame_principal,
                                                 fg_color=COR_BRANCO)
        self.card_data_nascimento.pack(fill='x', expand=True, pady=5, padx=20)
        #label data de nascimento
        self.label_data_nascimento = ctk.CTkLabel(self.card_data_nascimento,
                                                  text="📅 Data de Nascimento",
                                                  text_color=COR_AZUL,
                                                  font=("Arial", 12, "bold"))
        self.label_data_nascimento.pack(anchor="w")
        #data entry data de nascimento
        self.dataentry_data_nascimento = DateEntry(self.card_data_nascimento,
                                                   date_pattern = "dd/mm/yyyy",
                                                font=("Arial", 12, "bold"),
                                                background=COR_CINZA,
                                                foreground="white")
        self.dataentry_data_nascimento.pack(anchor='w')
        #card telefone
        self.card_telefone = ctk.CTkFrame(self.frame_principal,
                                          fg_color=COR_BRANCO)
        self.card_telefone.pack(fill='x', expand=True, pady=5, padx=20)
        #label telefone
        self.label_telefone = ctk.CTkLabel(self.card_telefone,
                                       text="📞 Telefone",
                                       text_color="#f0c609",
                                       font=("Arial", 12, "bold"))
        self.label_telefone.pack(anchor='w')
        #entry telefone
        self.entry_telefone = ctk.CTkEntry(self.card_telefone,
                                                placeholder_text="(11) 99999-9999",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA)
        self.entry_telefone.pack(anchor='w')
        #card email
        self.card_email = ctk.CTkFrame(self.frame_principal,
                                       fg_color=COR_BRANCO)
        self.card_email.pack(fill='x', expand=True, pady=5, padx=20)
        #label email
        self.label_email = ctk.CTkLabel(self.card_email,
                                               text="✉️E-mail",
                                               text_color="#2CCE6A",
                                               font=("Arial", 12, "bold"))
        self.label_email.pack(anchor='w')
        #entry email
        self.entry_email = ctk.CTkEntry(self.card_email,
                                                placeholder_text="maria@gmail.com",
                                                fg_color=COR_BRANCO,
                                                text_color=COR_CINZA)
        self.entry_email.pack(anchor='w')
        #card numero de documento
        self.card_numero_documento = ctk.CTkFrame(self.frame_principal,
                                                  fg_color=COR_BRANCO)
        self.card_numero_documento.pack(fill="x", expand=True,pady=5, padx=20)
        #label numero de documento
        self.label_numero_documento = ctk.CTkLabel(self.card_numero_documento,
                                         text="📄 Número de Documento (CPF ou RG)",
                                         text_color="#ff0000",
                                         font=("Arial", 12, "bold"))
        self.label_numero_documento.pack(anchor='w')
        #entry numero de documento
        self.entry_numero_documento = ctk.CTkEntry(self.card_numero_documento,
                                                   placeholder_text="000.000.000-00",
                                                   fg_color=COR_BRANCO,
                                                   text_color=COR_CINZA)
        self.entry_numero_documento.pack(anchor="w")
        #card para botao de salvar paciente
        self.card_salvar = ctk.CTkFrame(self.frame_principal,
                                        fg_color=COR_BRANCO)
        self.card_salvar.pack(fill='x', expand=True,pady=5, padx=20)
        #botao salvar atendimento
        self.botao_salvar_paciente = ctk.CTkButton(self.card_salvar,text="💾Salvar Paciente",
                                          text_color=COR_BRANCO,
                                          fg_color=COR_ROXO)
        self.botao_salvar_paciente.pack(fill='x', pady=10, padx=20)