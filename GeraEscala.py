from random import randint
from datetime import date, timedelta

pessoas = [];

while True:
  print('-'*10, 'Gerador de Escala', '-'*10)
  print('''
    1 - Adicionar Funcionários
    2 - Remover Funcionário
    3 - Gerar Escala
    4 - Exportar
    5 - Sair
  ''')
  opc = int(input('Informe a opção: '))
  if opc == 1:
    qtd = int(input('Informe a quantidade de funcionários a serem adicionados: '))
    for i in range(0, qtd):
      pessoas.append(str(input('Infome o nome do funcionário: ')).strip().title())
  elif opc == 2:
    if len(pessoas) > 0:
      print(f'|{"ID":^5}|{"Nome":^30}|')
      print('-'*38)
      for i, j in enumerate(pessoas):
        print(f'|{i:^5}|{j:^30}|')
    pessoas.pop(int(input('Informe o ID do funcionário a ser removido: ')))
  elif opc == 3:
    print(f'|{"Ordem":^5}|{"Nome":^30}|')
    print('-'*38)
    sorteado = []
    j = 0
    while len(sorteado) < len(pessoas):
      num = randint(0, len(pessoas)-1)
      if num not in sorteado:
        sorteado.append(num)
    for i in range(1, len(pessoas)+1):
      print(f'|{i:^5}|{pessoas[sorteado[j]]:^30}|')
      j += 1
  elif opc == 4:
    i = 0
    qtd = int(input('Quantos dias seram gerados: '))
    data = date.today()
    with open('escala.csv', 'w', encoding='UTF-8') as arq:
      arq.write(f'Data;Nome;Dia\n')
      while qtd > 0:
        dia_semana = data.weekday()
        dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
        if dia_semana not in {5, 6}:
          dataString = data.strftime('%d/%m/%Y')
          arq.write(f'{dataString};{pessoas[sorteado[i]]};{dias[dia_semana]}\n')
          data = data + timedelta(days=1)
          i += 1
          if i > len(pessoas)-1:
            i = 0
          qtd -= 1
        else:
          data = data + timedelta(days=1)
  elif opc == 5:
    break
  else:
    print('Opção Invalida!')