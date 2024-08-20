number = int(input('Digite um número: '))

if number % 2 == 0:
    print('Este número é par')
else:
    print('Este número é Ímpar')
    
age = int(input('Digite sua idade: '))

if 12 >= age >= 0:
    print('Criança')
elif 13 <= age <= 18:
    print('Adolescente')
else:
    print('Adulto')