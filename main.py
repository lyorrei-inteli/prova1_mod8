import re

# Função que é executada quando o usuário solicita informações sobre atualização de meio de pagamento
def payment_update():
    print('Você quer saber como atualizar o seu meio de pagamento.')

# Função que é executada quando o usuário solicita informações sobre acompanhamento de status de um pedido
def order_status():
    print('Você quer saber como acompanhar o status do seu pedido.')

# Dicionário de intenções em que a key representa uma expressão regular e o valor representa a ação que deve ser executada
intencoes = {
    r"(?:Como posso atualizar meu cartão de crédito?|Preciso mudar a forma de pagamento, o que fazer?|Quero atualizar minhas informações de pagamento|Método de pagamento desatualizado, como proceder para atualizar?)": "payment_update",
    r"(?:Onde vejo o status do meu pedido?|Como faço para rastrear meu pedido?|Quero saber onde está meu pedido|como faço?|Status de entrega|como consultar?)": "order_status"
}

# Dicionário de ações que faz um link da ação com a função que deve ser executada
acoes = {
        "payment_update": payment_update,
        "order_status": order_status
}

# Função que é executada quando o script inicia
def main():

    # Loop que permite que o usuário digite comandos repetidamente
    while True:
      
      # Linha para separar pedidos no terminal
      print('-------------------------------------')

      # Prompt de comando no terminal
      command = input("Digite o seu comando (caso deseje sair, digite \"sair\"): ")

      # Se o comando for igual a "sair", para o funcionamento do script
      if command == 'sair':
          break
      
      # Variável de checagem para ver se o comando que o usuário digitou corresponde a alguma expressão regular aceita pelo script
      understood = False
      
      # Loop em cada expressão regular
      for key, value in intencoes.items():
          
          # Checando se o comando que o usuário digitou faz correspondência com alguma expressâo regular
          pattern = re.compile(key)
          groups = pattern.findall(command)
          if groups:
            # Registra que o comando deu match com pelo menos uma expressão
            understood = True

            # Executa a função correspondente a aquela expressão
            acoes[value]()

      # Se nenhuma expressão regular corresponder ao comando do usuário, retornar um feedback
      if understood == False:
            print("Não entendi o seu comando, tente novamente!")
          
# Função que é executada quando o script inicia
if __name__ == "__main__":
    main()