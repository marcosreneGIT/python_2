# correção ex008
import os 

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('\nDigite uma letra: ')
   
    if len(letra_digitada) > 1:
        print('\nDigite apenas uma letra.')
        continue

    numero_tentativas += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('\nPalavra:', palavra_formada)


    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('\nVocê ganhou!!!')
        print('A palavra secreta era: ', palavra_formada)
        print('Tentativas: ', numero_tentativas)

        letras_acertadas = ''
        numero_tentativas = 0

        
