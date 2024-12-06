import streamlit as st
from views import View  

class AlterarDadosUI:
    @staticmethod
    def main():
        
        cliente_id = st.session_state.get("cliente_id")
        cliente_nome = st.session_state.get("cliente_nome")
        cliente_atual = View.cliente_listar_id(cliente_id)
        
        if cliente_atual is None:
            st.error("Erro: Usuário não encontrado.")
            return
        
        st.title("Alterar Dados")

        
        if cliente_nome == "admin":
            
            nova_senha = st.text_input("Nova Senha", type="password")
            if st.button("Alterar Senha"):
                cliente_atual.senha = nova_senha
                View.cliente_atualizar(cliente_id, cliente_atual.nome, cliente_atual.email, cliente_atual.fone, nova_senha)
                st.success("Senha alterada com sucesso!")
        else:
           
            novo_nome = st.text_input("Nome", cliente_atual.nome)
            novo_email = st.text_input("Email", cliente_atual.email)
            novo_fone = st.text_input("Telefone", cliente_atual.fone)
            nova_senha = st.text_input("Senha", cliente_atual.senha, type="password")
            
            if st.button("Salvar Alterações"):
                View.cliente_atualizar(cliente_id, novo_nome, novo_email, novo_fone, nova_senha)
                st.success("Dados alterados com sucesso!")
                st.session_state["cliente_nome"] = novo_nome  

