import requests
from datetime import datetime

def consultar_cotacao_moeda():
    """
    Consulta o valor de uma moeda em relação ao Real (BRL) usando a Awesome API
    e exibe dados como valor atual, máxima, mínima e última atualização.
    """
    
    # URL base da API para a cotação mais recente (latest)
    API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/"
    
    print("--- Consultor de Cotação de Moedas (Awesome API) ---")
    
    # 1. Solicitar a moeda ao usuário
    while True:
        # Ex: USD (Dólar), EUR (Euro), BTC (Bitcoin)
        moeda_codigo = input("Digite o código da moeda para cotar em BRL (ex: USD): ").strip().upper()
        
        if len(moeda_codigo) == 3 and moeda_codigo.isalpha():
            break
        else:
            print("Código inválido. Por favor, digite um código de 3 letras (ex: USD).")

    # 2. Montar a URL de consulta (Ex: .../last/USD-BRL)
    par_moeda = f"{moeda_codigo}-BRL"
    API_URL = API_BASE_URL + par_moeda
    
    print(f"Buscando cotação para {par_moeda}...")
    
    try:
        # 3. Realiza a requisição GET
        response = requests.get(API_URL, timeout=10) # Timeout para evitar espera infinita
        
        # Levanta uma exceção HTTPError se o status não for 200 (Sucesso)
        response.raise_for_status() 
        
        # Converte a resposta JSON para um dicionário Python
        dados = response.json()
        
        # 4. Tratar Moedas Inexistentes ou Retorno Vazio
        # O Awesome API retorna um JSON vazio {} ou um erro 404/500 se o par não existir.
        # Se a requisição foi 200, mas o JSON está incompleto, verificamos a chave.
        
        # A chave do JSON é o próprio par de moedas (ex: 'USDBRL')
        chave = moeda_codigo + "BRL"
        if chave not in dados:
            print(f"\n❌ FALHA! O par de moedas {par_moeda} não foi encontrado na API.")
            print("Verifique se o código da moeda está correto (ex: USD, EUR, BTC).")
            return
            
        cotacao = dados[chave]

        # 5. Extração e Exibição dos Dados (Sucesso)
        
        valor_compra = float(cotacao.get('bid')) # Valor de compra (bid) é o valor atual
        valor_maximo = float(cotacao.get('high'))
        valor_minimo = float(cotacao.get('low'))
        
        # Converte o timestamp Unix para um formato legível
        timestamp = int(cotacao.get('timestamp'))
        data_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y às %H:%M:%S')

        print("\n✅ Conexão bem-sucedida! Cotação atualizada:")
        print("==================================")
        print(f"Par de Moedas:     {moeda_codigo}/BRL")
        print(f"Valor de Compra:   R$ {valor_compra:.4f}") # 4 casas para maior precisão
        print(f"Máxima (24h):      R$ {valor_maximo:.4f}")
        print(f"Mínima (24h):      R$ {valor_minimo:.4f}")
        print(f"Última Atualização: {data_atualizacao}")
        print("==================================")
        
    except requests.exceptions.RequestException as e:
        # 6. Exibição de Falha (Erro de Conexão ou HTTP)
        print("\n❌ FALHA NA REQUISIÇÃO OU CONEXÃO.")
        print(f"Não foi possível obter a cotação. Detalhes do erro: {e}")
        print("Verifique sua conexão com a internet ou o endereço da API.")
    except ValueError:
        # Erro de conversão (se a API retornar um valor não numérico)
        print("\n❌ ERRO DE DADOS. A API retornou valores inesperados para a cotação.")


# Executa a função principal
if __name__ == "__main__":
    # Certifique-se de que a biblioteca 'requests' está instalada: pip install requests
    consultar_cotacao_moeda()