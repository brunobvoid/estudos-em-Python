# Ler valor do produto, escolher condição de Pagamento mostrar valor corrigido de acordo a condição escolhida
while True:
    p = float(input('Digite aqui o valor das compras: R$'))
    c = input('''Escolha a condição de pagamento:
1 - À vista (DINHEIRO ou PIX)
2 - À vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão
Digite aqui: ''')
    if c == '1':
        print('O Valor total a ser pago é de R${:.2f} com 10% de desconto'.format(p - (p * 10 / 100)))
        break
    elif c == '2':
        print('O Valor total a ser pago é de R${:.2f} com 5% de desconto'.format(p - (p * 5 / 100)))
        break
    elif c == '3':
        print('Pra dividir até 2x no cartão não tem alteração, segue o valor de R${:.2f} em 2x de R${:.2f}'.format(p, p/2))
        break
    elif c == '4':
        v = int(input('Pra quantas vezes vc quer dividir? '))
        print('O valor total da compra será de {:.2f} dividido pra {}x de {:.2f}'.format(p + (p * 20/100), v, (p + (p * 20/100)) / v ))
        break
    else:
        print('Opção Inválida, Tente Novamente!')
