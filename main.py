import re

def payment_update():
    print('Você quer saber como atualizar o seu meio de pagamento.')

def order_status():
    print('Você quer saber como acompanhar o status do seu pedido.')

intent_dict = {
    r"(?:Como posso atualizar meu cartão de crédito?|Preciso mudar a forma de pagamento, o que fazer?|Quero atualizar minhas informações de pagamento|Método de pagamento desatualizado, como proceder para atualizar?)": "payment_update",
    r"(?:Onde vejo o status do meu pedido?|Como faço para rastrear meu pedido?|Quero saber onde está meu pedido|como faço?|Status de entrega|como consultar?)": "order_status"
}

action_dict = {
        "payment_update": payment_update,
        "order_status": order_status
}

def main():
    while True:
      command = input("Digite o seu comando (caso deseje sair, digite \"sair\"): ")

      if command == 'sair':
          break
      
      understood = False
      
      for key, value in intent_dict.items():
          pattern = re.compile(key)
          groups = pattern.findall(command)
          if groups:
            understood = True
            action_dict[value]()

      if understood == False:
            print("Não entendi o seu comando, tente novamente!")
          

if __name__ == "__main__":
    main()