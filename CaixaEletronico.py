# Formatar título para visualização no terminal

def formatar_titulo(titulo):
    largura_terminal = 40
    lateral_terminal = (largura_terminal - (len(titulo))) // 2
    titulo_formatado = f'{lateral_terminal * " "} {titulo} {lateral_terminal * " "}'
    print('-' * largura_terminal)
    print(f'{titulo_formatado}')
    print('-' * largura_terminal)


# Função saque
    
def realizar_saque():
    try:
        valor_saque = int(input('Deseja sacar quantos reais? '
                                           '(Notas disponíveis: 100, 50, 20, 10, 5, 1) R$ '))
        if valor_saque <= 0:
            raise ValueError('Digite um valor válido.')

        total = valor_saque
        cedulas = [100, 50, 20, 10, 5, 1]

        for cedula_atual in cedulas:
            tot_cedula = total // cedula_atual
            total %= cedula_atual

            if tot_cedula > 0:
                print(f'Total de {tot_cedula} cédula(s) de R$ {cedula_atual}.')

        print('>' * 15)
        print('Fim da transação. Obrigado por utilizar nosso caixa eletrônico.')

    except ValueError as e:
        print(f'Erro: {e}')


def main():
    formatar_titulo('BANCO BRASILEIRO')
    realizar_saque()


if __name__ == '__main__':
    main()