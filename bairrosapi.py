import requests

def buscar_endereco_por_cep():
    """
    Solicita um CEP ao usuário, acessa a API ViaCEP e exibe o logradouro,
    bairro, cidade e estado correspondentes.
    """
    
    print("--- Buscador de Endereço por CEP (ViaCEP) ---")
    
    # 1. Solicitar e validar o CEP
    while True:
        cep = input("Digite o CEP (apenas números, 8 dígitos): ").strip()
        
        # O CEP deve ter exatamente 8 dígitos e ser composto apenas por números
        if len(cep) == 8 and cep.isdigit():
            break
        else:
            print("CEP inválido. Por favor, digite 8 dígitos numéricos.")

    # 2. Montar a URL da API
    # Formato da URL: https://viacep.com.br/ws/SEU_CEP/json/
    API_URL = f"https://viacep.com.br/ws/{cep}/json/"
    
    print(f"Buscando endereço para o CEP {cep}...")
    
    try:
        # 3. Realiza a requisição GET
        response = requests.get(API_URL)
        
        # Levanta uma exceção HTTPError se o status não for 200 (Sucesso)
        response.raise_for_status() 
        
        # Converte a resposta JSON para um dicionário Python
        dados = response.json()
        
        # 4. Trata CEPs Inexistentes
        # O ViaCEP retorna um JSON com a chave 'erro': true se o CEP não for encontrado
        if dados.get('erro'):
            print("\n❌ FALHA! CEP não encontrado na base de dados.")
            print("Verifique se o número do CEP está correto.")
            return

        # 5. Extração e Exibição dos Dados (Sucesso)
        
        logradouro = dados.get('logradouro', 'Não informado')
        bairro = dados.get('bairro', 'Não informado')
        cidade = dados.get('localidade', 'Não informado')
        estado = dados.get('uf', 'Não informado')
        
        print("\n✅ Conexão bem-sucedida! Endereço encontrado:")
        print("==================================")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro:     {bairro}")
        print(f"Cidade:     {cidade}")
        print(f"Estado:     {estado}")
        print("==================================")
        
    except requests.exceptions.RequestException as e:
        # 6. Exibição de Falha (Erro de Conexão ou HTTP)
        print("\n❌ FALHA NA CONEXÃO OU NA REQUISIÇÃO.")
        print(f"Não foi possível buscar o CEP. Detalhes do erro: {e}")
        print("Verifique sua conexão com a internet.")

# Executa a função principal
if __name__ == "__main__":
    # Certifique-se de que a biblioteca 'requests' está instalada: pip install requests
    buscar_endereco_por_cep()