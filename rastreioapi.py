import requests

def buscar_usuario_ficticio():
    """
    Acessa a API Random User Generator, busca um usuário fictício
    aleatório e exibe seu nome, e-mail e país.
    """
    
    API_URL = "https://randomuser.me/api/"
    
    print("--- Buscador de Usuário Fictício Aleatório ---")
    
    try:
        # 1. Realiza a requisição GET à API
        print(f"Buscando dados em: {API_URL}...")
        response = requests.get(API_URL)
        
        # 2. Verifica o status da resposta HTTP
        # O método raise_for_status() levanta uma exceção HTTPError se o status
        # não for 200 (Sucesso), permitindo que o bloco 'except' capture a falha.
        response.raise_for_status() 
        
        # 3. Converte a resposta JSON para um dicionário Python
        dados = response.json()
        
        # 4. Extração dos Dados
        # A API retorna um dicionário com uma chave 'results' que é uma lista
        usuario = dados['results'][0]
        
        # Nome completo
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        
        # E-mail
        email = usuario['email']
        
        # País
        pais = usuario['location']['country']
        
        # 5. Exibição dos Dados (Sucesso)
        print("\n✅ Conexão bem-sucedida! Usuário encontrado:")
        print("==================================")
        print(f"Nome:   {nome}")
        print(f"E-mail: {email}")
        print(f"País:   {pais}")
        print("==================================")
        
    except requests.exceptions.RequestException as e:
        # 6. Exibição de Falha (Erro de Conexão ou HTTP)
        print("\n❌ FALHA NA CONEXÃO OU NA REQUISIÇÃO.")
        print(f"Não foi possível buscar o usuário. Detalhes do erro: {e}")
        print("Verifique sua conexão com a internet ou o endereço da API.")

# Executa a função principal
if __name__ == "__main__":
    # Nota: Você pode precisar instalar a biblioteca requests se ainda não tiver:
    # pip install requests
    buscar_usuario_ficticio()