import psycopg2
from psycopg2 import OperationalError

def criar_conexao():
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="user_mail_cpf",
            user="juliano",
            password="senha123"
        )
        return conn
    except OperationalError as e:
        print("Erro ao conectar ao banco:", e)
        return None
