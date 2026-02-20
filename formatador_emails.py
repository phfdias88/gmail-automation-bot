import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import re
import os

def validar_email(email):
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex_email, email)

def processar_arquivo():
    # Criar uma janela oculta
    root = tk.Tk()
    root.withdraw()

    # Selecionar arquivo
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
    
    if not caminho_arquivo:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
        return

    try:
        df = pd.read_excel(caminho_arquivo)

        # Exibir colunas disponíveis
        colunas_disponiveis = "\n".join(df.columns)
        nome_coluna_email = simpledialog.askstring(
            "Escolher Coluna", 
            f"Digite o nome da coluna com os e-mails:\n\nColunas disponíveis:\n{colunas_disponiveis}"
        )

        if nome_coluna_email not in df.columns:
            messagebox.showerror("Erro", f"Coluna '{nome_coluna_email}' não encontrada.")
            return

        # Limpar e validar os e-mails
        lista_emails = df[nome_coluna_email].dropna().apply(lambda x: str(x).strip())
        lista_emails = [email for email in lista_emails if validar_email(email)]

        if not lista_emails:
            messagebox.showerror("Erro", "Nenhum e-mail válido encontrado.")
            return

        # Pedir nome do grupo
        group_name = simpledialog.askstring("Nome do Grupo", "Digite o nome do grupo:")

        if not group_name:
            messagebox.showerror("Erro", "Nome do grupo não fornecido.")
            return

        # Criar DataFrame para exportação
        df_emails = pd.DataFrame({
            "Group Email [Required]": [group_name] * len(lista_emails),
            "Member Email": lista_emails,
            "Member Type": ["User"] * len(lista_emails),
            "Member Role": ["Member"] * len(lista_emails)
        })

        # Nome do arquivo de saída
        nome_arquivo_saida = f"emails_{group_name}.csv"
        df_emails.to_csv(nome_arquivo_saida, index=False, sep=",", encoding='utf-8', quotechar='"')

        messagebox.showinfo("Sucesso", f"Arquivo '{nome_arquivo_saida}' criado com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo:\n{e}")

# Executar o processo
processar_arquivo()
