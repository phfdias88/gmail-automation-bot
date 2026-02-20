import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog
import re

def validar_email(email):
    # Verificar se o e-mail tem o formato válido
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex_email, email)

def processar_arquivo():
    # Abrir janela para selecionar o arquivo
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
    
    if not caminho_arquivo:
        print("Nenhum arquivo selecionado.")
        return

    try:
        # Carregar a planilha
        df = pd.read_excel(caminho_arquivo)

        # Pedir para o usuário inserir o nome da coluna manualmente
        root = tk.Tk()
        root.withdraw()
        nome_coluna_email = simpledialog.askstring("Escolher Coluna", f"Digite o nome da coluna com os e-mails de membros:")

        if nome_coluna_email not in df.columns:
            print(f"❌ Coluna '{nome_coluna_email}' não encontrada na planilha.")
            return

        # Extrair e-mails, remover espaços extras e filtrar e-mails válidos
        lista_emails = df[nome_coluna_email].dropna().apply(lambda x: str(x).strip())
        lista_emails = [email for email in lista_emails if validar_email(email)]

        if not lista_emails:
            print("❌ Nenhum e-mail válido encontrado.")
            return

        # Solicitar o nome do grupo
        group_name = simpledialog.askstring("Nome do Grupo", "Digite o nome do grupo:")

        if not group_name:
            print("❌ Nome do grupo não fornecido.")
            return

        # O nome do grupo será usado diretamente sem a verificação de e-mail
        group_email = f"{group_name}"  # O nome do grupo sem o domínio fixo

        # Definir os tipos e papéis de membros
        member_type = "User"  # Tipo de membro (geralmente "User")
        member_role = "Member"  # Papel de membro (geralmente "Member")

        # Criar DataFrame com as colunas solicitadas
        dados = {
            "Group Email [Required]": [group_email] * len(lista_emails),
            "Member Email": lista_emails,
            "Member Type": [member_type] * len(lista_emails),
            "Member Role": [member_role] * len(lista_emails)
        }

        df_emails = pd.DataFrame(dados)

        # Salvar como CSV, utilizando vírgula como separador
        nome_arquivo_saida = "emails_formatados_gmail.csv"
        df_emails.to_csv(nome_arquivo_saida, index=False, sep=",", encoding='utf-8', quotechar='"')

        print(f"✅ Arquivo '{nome_arquivo_saida}' criado com sucesso!")
        print("Agora você pode fazer o upload deste arquivo no Google Groups.")

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo: {e}")

# Criar janela para selecionar o arquivo
root = tk.Tk()
root.withdraw()
processar_arquivo()
