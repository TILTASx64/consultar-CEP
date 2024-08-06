# Bibliotecas utilizadas
import os, requests, json

# Criando a função
def consultar(cep):
    try:
        req = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        req.raise_for_status()  # Levanta um erro se a requisição falhar
        cp = req.json()

        if 'erro' in cp:
            print("CEP inválido. Tente novamente.")
            return

        # Imprimindo resultado na tela
        print("______________________________________________________________")
        print("---------------------Consulta do CEP v1.0---------------------")

        print(f"Cep: {cp.get('cep', 'Não disponível')}")
        print(f"Logradouro: {cp.get('logradouro', 'Não disponível')}")
        print(f"Complemento: {cp.get('complemento', 'Não disponível')}")
        print(f"Bairro: {cp.get('bairro', 'Não disponível')}")
        print(f"Cidade: {cp.get('localidade', 'Não disponível')}")
        print(f"Estado: {cp.get('uf', 'Não disponível')}")
        print(f"DDD: {cp.get('ddd', 'Não disponível')}")
        
        print("______________________________________________________________")
        print("-----------------------Fim da Consulta------------------------")

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar o serviço. Tente novamente mais tarde.")
        print(e)

# Loop principal
while True:
    # Clear da tela (cls para Windows, clear para Unix)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Solicitando entrada do usuário(a)
    entrada = input("Digite o CEP (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        print("Encerrando o programa.")
        break

    # Chamando a função
    consultar(entrada)

    # Perguntando se o usuário deseja realizar outra consulta
    continuar = input("Deseja realizar outra consulta? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando o programa.")
        break
