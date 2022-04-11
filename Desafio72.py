# res = 0
# num = int(input("Introduza um número de 0 a 20: "))
# num_extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis',
# 'Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze',
# 'Dezasseis','Dezassete','Dezoito','Dezanove','Vinte')
# while True:
#     for i in range(len(num_extenso)):
#         if i == num:
#             res = num_extenso[i]
#         if num < 0 or num > 20:
#             num = int(input("Tente novamente, introduza um número de 0 a 20: "))
#     print(f"O {num} por extenso é {res}")
#     break

num_extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis',
                'Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze',
                'Dezasseis','Dezassete','Dezoito','Dezanove','Vinte')
while True:
    num = int(input("Introduza um número de 0 a 20: "))
    if 0 <= num <= 20:
        print(f"O {num} por extenso é {num_extenso[num]}")
    print("Tente novamente, ", end="")
    escolha = ' '
    while escolha not in 'sn':       
        escolha = input("Deseja continuar?[S/N]").strip().lower()[0]
    if escolha == 'n':
        break
