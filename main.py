import streamlit as st
from conexao import criar_conexao

st.title("Cadastro de Usuários")

# Inicializa session_state
for campo in ["nome", "email", "cpf"]:
    if campo not in st.session_state:
        st.session_state[campo] = ""

# Função para salvar no banco
def salvar_dados():
    conn = criar_conexao()
    if conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO usuarios (nome, email, cpf) VALUES (%s, %s, %s)",
                    (st.session_state["nome"], st.session_state["email"], st.session_state["cpf"])
                )
                conn.commit()
                st.success("Cadastro salvo com sucesso!")
            except Exception as e:
                st.error(f"Erro ao salvar no banco: {e}")
            finally:
                conn.close()
    else:
        st.error("Não foi possível conectar ao banco.")

# Função para mostrar todos os cadastros
def mostrar_cadastros():
    conn = criar_conexao()
    if conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("SELECT nome, email, cpf FROM usuarios;")
                resultados = cursor.fetchall()
                if resultados:
                    st.subheader("Cadastros existentes")
                    st.table(resultados)
                else:
                    st.info("Nenhum cadastro encontrado.")
            except Exception as e:
                st.error(f"Erro ao buscar cadastros: {e}")
            finally:
                conn.close()

# Inputs do usuário
st.text_input("Nome", key="nome")
st.text_input("Email", key="email")
st.text_input("CPF", key="cpf")

# Botão para salvar
if st.button("Salvar Cadastro"):
    salvar_dados()

# Mostrar cadastros existentes
mostrar_cadastros()
