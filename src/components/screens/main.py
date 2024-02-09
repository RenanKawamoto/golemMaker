import tkinter as tk
from tkinter import ttk

class SistemaDinamico:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Dinâmico")

        self.campos = []
        self.criar_widgets()

    def criar_widgets(self):
        # Label e Entry para o tipo
        self.label_tipo = tk.Label(self.janela, text="Selecione o tipo:")
        self.label_tipo.grid(row=0, column=0, padx=5, pady=5)

        self.opcoes_tipo = ["Texto", "Número", "Data"]  # Adicione mais tipos conforme necessário
        self.tipo_var = tk.StringVar()
        self.dropdown_tipo = ttk.Combobox(self.janela, textvariable=self.tipo_var, values=self.opcoes_tipo)
        self.dropdown_tipo.grid(row=0, column=1, padx=5, pady=5)
        self.dropdown_tipo.set(self.opcoes_tipo[0])

        # Botão para adicionar campo
        self.botao_adicionar = tk.Button(self.janela, text="Adicionar Campo", command=self.adicionar_campo)
        self.botao_adicionar.grid(row=0, column=2, padx=5, pady=5)

        # Botão para finalizar e salvar
        self.botao_finalizar = tk.Button(self.janela, text="Finalizar e Salvar", command=self.finalizar_e_salvar)
        self.botao_finalizar.grid(row=0, column=3, padx=5, pady=5)

    def adicionar_campo(self):
        # Adiciona um novo campo (Label, Entry, Dropdown) dinamicamente
        novo_campo = {}
        
        # Label e Entry para o valor
        label_nome = tk.Label(self.janela, text="Valor:")
        label_nome.grid(row=len(self.campos) + 1, column=0, padx=5, pady=5)
        
        entry_valor = tk.Entry(self.janela)
        entry_valor.grid(row=len(self.campos) + 1, column=1, padx=5, pady=5)
        
        # Dropdown para o tipo
        dropdown_tipo_campo = ttk.Combobox(self.janela, values=self.opcoes_tipo)
        dropdown_tipo_campo.grid(row=len(self.campos) + 1, column=2, padx=5, pady=5)
        dropdown_tipo_campo.set(self.opcoes_tipo[0])

        novo_campo['nome'] = entry_valor
        novo_campo['tipo'] = dropdown_tipo_campo

        self.campos.append(novo_campo)

    def finalizar_e_salvar(self):
        # Coleta todas as informações e salva em um arquivo de texto
        with open('informacoes.txt', 'w') as arquivo:
            for campo in self.campos:
                valor = campo['nome'].get()
                tipo = campo['tipo'].get()
                arquivo.write(f"{tipo}: {valor}\n")

        self.janela.destroy()

if __name__ == "__main__":
    janela_principal = tk.Tk()
    sistema = SistemaDinamico(janela_principal)
    janela_principal.mainloop()
