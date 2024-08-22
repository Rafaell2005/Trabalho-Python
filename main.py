#sequência de fibonacci//
N = int(input('Qual numero dejesa usar: '))
A = 0
B = 1

while A <= N:
    print(A)
    A, B = B, A+B

#######################################################################################################################################################################  
#######################################################################################################################################################################  


#Numero Primo Gemeos//
N = 1001

while True:
    N1 = True
    if N <= 1:
        N1 = False
    elif N == 2 or N == 3:
        N1 = True
    elif N % 2 == 0 or N % 3 == 0:
        N1 = False
    else:
        i = 5
        while i * i <= N:
            if N % i == 0 or N % (i + 2) == 0:
                N1 = False
                break
            i += 6
    N2 = True
    if (N + 2) <= 1:
        N2 = False
    elif (N + 2) == 2 or (N + 2) == 3:
        N2 = True
    elif (N + 2) % 2 == 0 or (N + 2) % 3 == 0:
        N2 = False
    else:
        i = 5
        while i * i <= (N + 2):
            if (N + 2) % i == 0 or (N + 2) % (i + 2) == 0:
                N2 = False
                break
            i += 6
    if N1 and N2:
        print(f"O primeiro par de primos gêmeos maiores que 1000 é: ({N}, {N + 2})")
        break
    
    N += 1

#########################################################################################################################################################################
#######################################################################################################################################################################  


    #Palindromo ou nao//
frase = input('Escreva uma frase: ')

frase_processada = ''

for char in frase:
    if 'A' <= char <= 'Z':
        char = chr(ord(char) + 32)
    
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
        'ç': 'c',
        'Á': 'a', 'À': 'a', 'Ã': 'a', 'Â': 'a',
        'É': 'e', 'È': 'e', 'Ê': 'e',
        'Í': 'i', 'Ì': 'i', 'Î': 'i',
        'Ó': 'o', 'Ò': 'o', 'Õ': 'o', 'Ô': 'o',
        'Ú': 'u', 'Ù': 'u', 'Û': 'u',
        'Ç': 'c'
    }
    
    if char in acentos:
        char = acentos[char]
    
    if char != ' ':
        frase_processada += char

if frase_processada == frase_processada[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

#########################################################################################################################################################################
#######################################################################################################################################################################  


#Criptografar em cifra de cesar//
texto = input("Digite a mensagem para ser criptografada: ")
n = int(input("Digite a valor da chave: "))

alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem_criptografada = ''

for char in texto:
    if char in alfabeto:
        posicao_atual = alfabeto.index(char)
        
        nova_posicao = (posicao_atual + n) % 26  
        
        mensagem_criptografada += alfabeto[nova_posicao]
    else:
        mensagem_criptografada += char

print("Mensagem criptografada:", mensagem_criptografada)
