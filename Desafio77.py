palavras = ('aprender','python','programador','correr','curso',
'linguagem','trabalhar','estudar','gratis','futuro','praticar',
'mercado','computador','internet')

for p in palavras:
     print(f'\nNa palavra "{p.upper()}" temos -> ', end='')
     for letra in p:
         if letra.lower() in 'aeiou':
             print(letra.upper(), end=' ')