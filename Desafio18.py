from math import radians,sin,cos,tan
ang = float(input("Digite um angulo: "))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tang = tan(radians(ang))
print(f"O angulo é {ang}\nO seu conseno é de {coseno:.2f}\nO seno é de {seno:.2f}\nA tangente é {tang:.2f}")