# Cadastro de Usuários - Streamlit + PostgreSQL

Este projeto é um aplicativo web simples desenvolvido em **Python** usando **Streamlit** para a interface e **PostgreSQL** para o armazenamento de dados. Permite cadastrar usuários com **nome, email e CPF** e exibir todos os cadastros em uma tabela.

---

## 🛠 Tecnologias utilizadas

- Python 3.10+  
- Streamlit  
- PostgreSQL  
- psycopg2-binary  

---

## 🚀 Funcionalidades

1. Cadastro de usuários com nome, email e CPF.  
2. Armazenamento seguro no banco PostgreSQL.  
3. Visualização de todos os cadastros em tempo real.  
4. Campos mantidos em memória enquanto a sessão está ativa (session_state).

---

## 📁 Estrutura do projeto

projeto_streamlit/
│
├── main.py # App principal Streamlit
├── conexao.py # Conexão com PostgreSQL
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo

💻 Como rodar o projeto

## Crie e ative um ambiente virtual:

python -m venv env
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows


## Instale as dependências:

pip install -r requirements.txt


## Execute o aplicativo:

streamlit run main.py


## Abra o navegador no link que aparecer no terminal (geralmente http://localhost:8501).

👨‍💻 Autor

Juliano Aragão