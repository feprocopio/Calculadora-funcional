from time import sleep
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('===' * 10)
    print(' [1] Somar\n [2] Multiplicar\n [3] Maior numero\n [4] Novos números\n [5] Sair do programa')
    opção = int(input('>>>> Qual sua opção?'))
    if opção == 1:
        print('A soma entre {} e {} é {}'.format(p1, p2, p1 + p2))
    elif opção == 2:
        m = p1 * p2
        print('A mulpiplicação de {} x {} é {}'.format(p1, p2, m))
    elif opção == 3:
        if p1 > p2:
            maior = p1
        else:
            maior = p2
        print('O numero {} é o maior'.format(maior))
    elif opção == 4:
        print('Informe os numeros novamente:')
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida')
        sleep(3)
print('Fim do programa, volte sempre!!!')

