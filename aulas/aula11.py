'''
Cores no terminal

ANSI
escape sequence \

\033[0;00;00m       ''      033[m

style fonte         text color          backgorund color
0 none              30 white            40 white
1 bold              31 red              41 red
4 underline         32 green            42 green
7 negative          33 yellow           43 yellow
                    34 dark blue        44 dark blue
                    35 purple           45 purple
                    36 blue             46 blue
                    37 gray             47 gray

' \033[0;30;41m             \033[m '
' \033[4;33;46m             \033[m '
' \033[1;35;43m             \033[m '
' \033[0;30;42m             \033[m '
' \033[0;00;00m             \033[m '
' \033[7;00;00m             \033[m '
' \033[0;30;00m             \033[m '




cores = {    #cores normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;30;m',

                #cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;30m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               #cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;30m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano


print('\033[7;30mOlá Python\033[m')
a = 'Feliz'
b = 'Ano Novo'
print(f'\033[1;31;40m{a}\033[m\033[7;31;40m{b}\033[m')
# dá pra colocar dentro do {} das variaveis também esse código de cor

dá também para criar um dicionario de cores
cor = {'azul':'\033[34m',
        'amarelo':'\033[033m'}
'''
