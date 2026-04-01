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

class NovoAtendimento(ctk.CTkFrame):
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
        self.label_novo_atendimento = ctk.CTkLabel(self.frame_titulo,
                                                   text="Novo Atendimento",
                                                   text_color=COR_BRANCO,
                                                   font=("Arial", 24, "bold"))
        self.label_novo_atendimento.pack()

        self.label_registre_detalhes = ctk.CTkLabel(self.frame_titulo,
                                                    text="Registre os detalhes do Atendimento",
                                                    text_color=COR_BRANCO,
                                                    font=('Arial', 12, 'bold'))
        self.label_registre_detalhes.pack()
        #frame principal
        self.frame_principal = ctk.CTkFrame(self, fg_color=COR_BRANCO,
                                            corner_radius=20,
                                            width=400)
        self.frame_principal.grid(row=1, column=0, pady=20, padx=20)
        #card paciente
        self.card_paciente = ctk.CTkFrame(self.frame_principal,
                                          fg_color=COR_BRANCO)
        self.card_paciente.pack(fill="x", expand=True, pady=5, padx=20)
        #label paciente
        self.label_paciente = ctk.CTkLabel(self.card_paciente,
                                           text="Paciente",
                                           text_color=COR_ROXO,
                                           font=("Arial", 12, "bold"))
        self.label_paciente.pack(anchor='w')
        #entry paciente
        self.entry_paciente = ctk.CTkEntry(self.card_paciente,
                                           placeholder_text="Nome do Paciente",
                                           fg_color=COR_BRANCO,
                                           text_color=COR_CINZA)
        self.entry_paciente.pack(anchor="w")
        #data de atendimento
        self.card_data = ctk.CTkFrame(self.frame_principal,
                                      fg_color=COR_BRANCO)
        self.card_data.pack(fill='x', expand=True,pady=5, padx=20)
        #label data de atendimento
        self.label_data = ctk.CTkLabel(self.card_data,
                                       text='📅Data de Atendimentos',
                                       text_color=COR_AZUL,
                                       font=('Arial', 12, 'bold'))
        self.label_data.pack(anchor='w')
        #data entry data de atendimento
        self.data_entry_atendimento = DateEntry(self.card_data,
                                                date_pattern = "dd/mm/yyyy",
                                                font=("Arial", 12, "bold"),
                                                background=COR_CINZA,
                                                foreground="white")
        self.data_entry_atendimento.pack(anchor="w")
        #card tipo de atendimento
        self.card_tipo_atendimento = ctk.CTkFrame(self.frame_principal,
                                                  fg_color=COR_BRANCO)
        self.card_tipo_atendimento.pack(fill='x', expand=True,pady=5, padx=20)

        #label tipo de atendimento
        self.label_tipo = ctk.CTkLabel(self.card_tipo_atendimento,
                                       text="📋 Tipo de Atendimento",
                                       text_color="#f0c609",
                                       font=("Arial", 12, "bold"))
        self.label_tipo.pack(anchor='w')
        #combobox tipo de atendimento
        self.combobox_tipo = ctk.CTkComboBox(self.card_tipo_atendimento,fg_color=COR_BRANCO,text_color='black',
                                             values=["Consulta",
                                                     "Retorno",
                                                     "Avaliação",
                                                     "Exame",
                                                     "Procedimento"],
                                                     state='readonly',
                                                     font=("Arial", 12, "bold"))
        self.combobox_tipo.pack(anchor="w")

        #card obsrvacoes do profissional
        self.card_observacoes = ctk.CTkFrame(self.frame_principal,
                                              fg_color=COR_BRANCO)
        self.card_observacoes.pack(fill='x', expand=True,pady=5, padx=20)
        #label observacoes do profissional
        self.label_observacoes = ctk.CTkLabel(self.card_observacoes,
                                               text="📓 Observações do Profissional",
                                               text_color="#2CCE6A",
                                               font=("Arial", 12, "bold"))
        self.label_observacoes.pack(anchor='w')
        #text observacoes do profissional
        self.text_observacoes = ctk.CTkTextbox(self.card_observacoes,
                                               border_width=2,
                                               border_color=COR_CINZA,
                                               fg_color=COR_BRANCO)
        self.text_observacoes.pack(fill='x')
        #card status de atendimento
        self.card_status = ctk.CTkFrame(self.frame_principal,
                                        fg_color=COR_BRANCO)
        self.card_status.pack(fill='x', expand=True,pady=5, padx=20)
        #label status de atendimento
        self.label_status = ctk.CTkLabel(self.card_status,
                                         text="✅ Status de Atendimento",
                                         text_color="#ff0000",
                                         font=("Arial", 12, "bold"))
        self.label_status.pack(anchor="w")
        #combo box status de atendimento
        self.combo_status = ctk.CTkComboBox(self.card_status,fg_color=COR_BRANCO,text_color='black',
                                             values=["Realizado",
                                                     "Em Acompanhamento"],
                                                     state='readonly',
                                                     font=("Arial", 12, "bold"))
        self.combo_status.pack(anchor="w")
        #card para botao de salvar atendimento
        self.card_salvar = ctk.CTkFrame(self.frame_principal,
                                        fg_color=COR_BRANCO)
        self.card_salvar.pack(fill='x', expand=True,pady=5, padx=20)
        #botao salvar atendimento
        self.botao_salvar = ctk.CTkButton(self.card_salvar,text="💾Salvar Atendimento",
                                          text_color=COR_BRANCO,
                                          fg_color=COR_ROXO)
        self.botao_salvar.pack(fill='x')