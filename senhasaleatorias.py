import random
import string

def gerar_senha_segura():
    """
    Gera uma senha aleatória com base no tamanho escolhido pelo usuário,
    incluindo letras, números e símbolos.
    """
    
    # Define todos os caracteres possíveis
    # string.ascii_letters: a-z e A-Z
    # string.digits: 0-9
    # string.punctuation: !, ", #, $, %, etc.
    todos_caracteres = string.ascii_letters + string.digits + string.punctuation
    
    print("--- Gerador de Senhas Seguras ---")

    # 1. Solicita e valida o tamanho da senha
    while True:
        try:
            tamanho = int(input("Digite o tamanho desejado para a senha (ex: 12): "))
            
            # Um tamanho mínimo razoável para senhas seguras
            if tamanho >= 8:
                break
            elif tamanho > 0:
                print("Recomendamos um tamanho de pelo menos 8 caracteres para segurança.")
                # Permite que o usuário continue, mas avisa
                break
            else:
                print("O tamanho da senha deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # 2. Garante que pelo menos um de cada tipo seja incluído (Melhorando a segurança)
    
    # Criamos a senha garantindo pelo menos 1 de cada tipo
    senha_base = [
        random.choice(string.ascii_lowercase), # Pelo menos uma minúscula
        random.choice(string.ascii_uppercase), # Pelo menos uma maiúscula
        random.choice(string.digits),          # Pelo menos um número
        random.choice(string.punctuation)      # Pelo menos um símbolo
    ]
    
    # 3. Preenche o restante da senha (se o tamanho for maior que 4)
    # Subtraímos 4 porque 4 caracteres já foram garantidos
    caracteres_restantes = tamanho - len(senha_base)
    
    if caracteres_restantes > 0:
        # Adiciona o restante dos caracteres aleatoriamente
        senha_base.extend(random.choice(todos_caracteres) for _ in range(caracteres_restantes))
        
    # 4. Embaralha a lista de caracteres para garantir aleatoriedade
    random.shuffle(senha_base)
    
    # 5. Converte a lista de volta para uma string
    senha_final = "".join(senha_base)

    # 6. Exibe o resultado
    print("\n==================================")
    print(f"Tamanho da Senha: {tamanho}")
    print(f"Sua Nova Senha Segura: {senha_final}")
    print("==================================")

# Executa a função principal
if __name__ == "__main__":
    gerar_senha_segura()