# Função     
def contaVogais(frase):
      vogais = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
      nVogais = 0
      for letra in frase:
            if letra in vogais:
                  nVogais += 1
      print(f'Quantidade de Vogais:{nVogais}')
      return None

# Programa Principal
lida = input("Diga a frase: ")
contaVogais(lida)
