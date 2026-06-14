# 📧 Gmail Automation Bot

Ferramenta em **Python** com interface gráfica que automatiza a preparação de listas de e-mails para importação em massa no **Google Groups**. A partir de uma planilha Excel, o programa valida os endereços e gera um arquivo CSV já no formato esperado pelo Google Workspace.

## ✨ Funcionalidades

- 📂 Leitura de planilhas Excel (`.xlsx` / `.xls`) via interface gráfica (Tkinter).
- ✅ Validação automática de e-mails por expressão regular.
- 🧹 Limpeza dos dados (remoção de espaços e valores vazios).
- 📤 Exportação para CSV no formato de importação de membros do Google Groups (`Group Email`, `Member Email`, `Member Type`, `Member Role`).
- 🖱️ Uso simples por diálogos: selecionar arquivo, escolher coluna e nomear o grupo.

## 🛠️ Tecnologias

- **Python**
- **Pandas** — leitura de Excel e manipulação de dados
- **Tkinter** — interface gráfica
- **re** (regex) — validação de e-mails

## 🚀 Como executar

Pré-requisitos: Python 3 instalado.

```bash
git clone https://github.com/phfdias88/gmail-automation-bot.git
cd gmail-automation-bot

pip install pandas openpyxl

python formatador_emails.py
```

Ao executar, uma janela permitirá selecionar a planilha, escolher a coluna de e-mails e informar o nome do grupo. O arquivo `emails_<nome-do-grupo>.csv` será gerado na pasta atual.

## 👤 Autor

**Paulo Henrique Ferreira Dias** — [LinkedIn](https://www.linkedin.com/in/phdias-ti)
