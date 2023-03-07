# Ler peso e altura, calcular IMC mostrar resultado de acordo tabela
print('Vamos caucular seu IMC')
p = float(input('Informe seu peso em kg: '))
a = float(input('Informe sua altura em m: '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} e você está no peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f} e você está com Obesidade!'.format(imc))
else:
    print('Seu IMC é {:.2} e você está com Obesidade Morbida'.format(imc))
