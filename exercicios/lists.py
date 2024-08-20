# 1 - Crie uma lista para cada informação a seguir:
#     Lista de números de 1 a 10;
#     Lista com quatro nomes;
#     Lista com o ano que você nasceu e o ano atual.
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


nums = [1,2,3,4,5,6,7,8,9,10]
teams = ["Vasco", "Flamengo", "Botafogo", "Fluminense"]
years = [1991, 2024]

for num in nums:
    print(num)
    
oddSum=0
for num in nums:
    if num % 2 == 1:
        oddSum += num
print(f"Soma de números ímpares: {oddSum}")    

num = int(input('Digite um número aleatório: '))
print("--------- TABUADA----------")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")