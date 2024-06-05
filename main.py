# verificar quantas vogais e quantas consoantes foram digitadas
x = input('Digite a frase ou palavra que deseja verificar a quantidade de vogais e consoantes ')
vogais = 0
consoantes = 0

for i in x:
    if i.lower() in 'aeiou':
        vogais = vogais + 1

    elif i.lower() in 'bcdfghijklmnopqrstvwxyz':
        consoantes = consoantes + 1

print(f'Foram digitadas {vogais} vogais.')
print(f'Foram digitadas {consoantes} consoantes.')
