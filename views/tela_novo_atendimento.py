import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import messagebox as mg
from models.atendimentos import Atendimento
from views.tela_pacientes import TelaPaciente
from controllers.atendimento_controller import adicionar_atendimento
from controllers.paciente_controller import listar_pacientes
from pathlib import Path
from PIL import Image

COR_ROXO = "#7c3aed" #Sidebar, botões principais, ícones
COR_AZUL = "#3b82f6" #Cards, destaques, status
COR_BRANCO ="#ffffff" #Fundo dos cards, superfícies
COR_CINZA_CLARO = "#f9fafb" #Fundo da página
COR_CINZA = "#808080" #Fundo da página
COR_CINZA_ESCURO = "#111827" #Textos e títulos

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_IMG_SAVE = BASE_DIR / "assets" / "diskette.png"

class NovoAtendimento(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=COR_BRANCO, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.pacientes = listar_pacientes()
        self.pacientes_dict = {p["nome"]: p["id"] for p in self.pacientes}
        #frame titulo
        self.frame_titulo = ctk.CTkFrame(self,
                                         fg_color=COR_BRANCO)
        self.frame_titulo.grid(row=0, column=0, pady=20)
        #labels titulo
        diskett = ctk.CTkImage(light_image=Image.open(PATH_IMG_SAVE),
                            dark_image=Image.open(PATH_IMG_SAVE),
                            size=(30, 30))
        self.emoji_titulo = ctk.CTkLabel(self.frame_titulo,
                                         image=diskett, text='')
        self.emoji_titulo.pack()
        self.label_novo_atendimento = ctk.CTkLabel(self.frame_titulo,
                                                   text="Novo Atendimento",
                                                   text_color=COR_ROXO,
                                                   font=("Arial", 28, "bold"))
        self.label_novo_atendimento.pack()

        self.label_registre_detalhes = ctk.CTkLabel(self.frame_titulo,
                                                    text="Registre os detalhes do Atendimento",
                                                    text_color=COR_ROXO,
                                                    font=('Arial', 12, 'bold'))
        self.label_registre_detalhes.pack()
        #frame centro
        self.frame_centro = ctk.CTkFrame(self, fg_color=COR_BRANCO)
        self.frame_centro.grid(row=1, column=0, sticky="nsew")
        self.frame_centro.grid_columnconfigure(0, weight=1)
        self.frame_centro.grid_rowconfigure(0, weight=1)
        #frame principal
        self.frame_principal = ctk.CTkFrame(self.frame_centro, fg_color=COR_ROXO,
                                            corner_radius=20,
                                            border_width=1,
                                            border_color="#e5e7eb",
                                            width=750,
                                            height=620)
        self.frame_principal.pack(expand=True, padx=80, pady=10)
        self.frame_principal.pack_propagate(False)
        #card paciente
        self.card_paciente = self.criar_card("Paciente", COR_BRANCO)
        #entry paciente
        self.combobox_paciente = ctk.CTkComboBox(
            self.card_paciente,fg_color=COR_BRANCO,text_color='black',button_hover_color="#6d28d9",
            dropdown_fg_color=COR_BRANCO, dropdown_hover_color=COR_AZUL, dropdown_text_color=COR_CINZA_ESCURO,
            values=list(self.pacientes_dict.keys()),border_color=COR_BRANCO,border_width=1.5,height=36,
            state="readonly"
        )
        self.combobox_paciente.pack(fill="x")
        #card data de atendimento
        self.card_data = self.criar_card('📅Data de Atendimento', COR_BRANCO)
        #data entry data de atendimento
        self.data_entry_atendimento = DateEntry(self.card_data,
                                                date_pattern = "dd/mm/yyyy",
                                                font=("Arial", 12, "bold"),
                                                background=COR_CINZA,
                                                foreground="white",border_color=COR_BRANCO,border_width=1.5)
        self.data_entry_atendimento.pack(fill="x")
        #card tipo de atendimento
        self.card_tipo_atendimento = self.criar_card("📋 Tipo de Atendimento", COR_BRANCO)
        #combobox tipo de atendimento
        self.combobox_tipo = ctk.CTkComboBox(self.card_tipo_atendimento,fg_color=COR_BRANCO,text_color='black',button_hover_color="#6d28d9",
            dropdown_fg_color=COR_BRANCO, dropdown_hover_color=COR_AZUL, dropdown_text_color=COR_CINZA_ESCURO,
                                             values=["Consulta",
                                                     "Retorno",
                                                     "Avaliação",
                                                     "Exame",
                                                     "Procedimento"],
                                                     state='readonly',
                                                     font=("Arial", 12, "bold"),
                                                     height=36,border_color=COR_BRANCO,border_width=1.5)
        self.combobox_tipo.pack(fill="x")

        #card obsrvacoes do profissional
        self.card_observacoes = self.criar_card("📓 Observações do Profissional", COR_BRANCO)
        #text observacoes do profissional
        self.text_observacoes = ctk.CTkTextbox(self.card_observacoes,
                                               border_width=2,
                                               text_color=COR_CINZA_ESCURO,
                                               border_color=COR_CINZA,
                                               fg_color=COR_BRANCO,
                                               height=70)
        self.text_observacoes.pack(fill='x')
        #card status de atendimento
        self.card_status = self.criar_card("✅ Status de Atendimento", COR_BRANCO)
        #combo box status de atendimento
        self.combo_status = ctk.CTkComboBox(self.card_status,fg_color=COR_BRANCO,text_color='black',button_hover_color="#6d28d9",
            dropdown_fg_color=COR_BRANCO, dropdown_hover_color=COR_AZUL, dropdown_text_color=COR_CINZA_ESCURO,
                                             values=["Realizado",
                                                     "Em Acompanhamento"],
                                                     state='readonly',
                                                     font=("Arial", 12, "bold"),
                                                height=36,border_color=COR_BRANCO,border_width=1.5)
        self.combo_status.pack(fill="x")
        #card para botao de salvar atendimento
        self.card_salvar = ctk.CTkFrame(self.frame_principal,
                                        fg_color=COR_ROXO)
        self.card_salvar.pack(fill='x',pady=10, padx=20)
        #botao salvar atendimento
        self.botao_salvar = ctk.CTkButton(self.card_salvar,text="💾Salvar Atendimento",
                                          font=("Arial", 16, "bold"),
                                          text_color=COR_BRANCO,
                                          fg_color=COR_AZUL,
                                          corner_radius=10,
                                          height=40, width=500,
                                          command=self.salvar_atendimento)
        self.botao_salvar.pack(fill='x')
    def criar_card(self, texto, cor):
        card = ctk.CTkFrame(self.frame_principal, fg_color=COR_ROXO)
        card.pack(fill="x", pady=10, padx=20)

        label = ctk.CTkLabel(card,text=texto,
                                  text_color=cor,
                                  font=("Arial",14,"bold"))
        label.pack(anchor="w")
        return card
    def salvar_atendimento(self):

        nome_paciente = self.combobox_paciente.get()
        data = self.data_entry_atendimento.get()
        tipo = self.combobox_tipo.get()
        observacoes = self.text_observacoes.get("1.0", "end").strip()
        status = self.combo_status.get()
        if not nome_paciente:
            mg.showerror("Erro", "Paciente não encontrado")
            return
        if not tipo:
            mg.showerror("Erro", "Selecione o tipo de atendimento")
            return
        if not status:
            mg.showerror("Erro", "Selecione o status")
            return
        paciente_id = self.pacientes_dict.get(nome_paciente)
        atendimento = Atendimento(
            id=0,
            paciente_id=paciente_id,
            data=data,
            tipo=tipo,
            observacoes=observacoes,
            status=status
        )
        adicionar_atendimento(atendimento)
        mg.showinfo("Sucesso", "Atendimento cadastrado com sucesso!")
        self.limpar_campos()
        self.master.master.mostrar_atendimento()
    def limpar_campos(self):
        self.combobox_paciente.set("")
        self.combobox_tipo.set("")
        self.text_observacoes.delete("1.0", "end")
        self.combo_status.set("")