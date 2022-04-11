from datetime import date
print("Coloque 0 para ver o ano actual:")
ano = int(input("Introduza um ano:"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")