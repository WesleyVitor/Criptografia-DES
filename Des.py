'''
    Algoritmo DES

    Aluno: Wesley Vitor silva de Morais
    Curso: BSI - UFRN Ceres Caicó
    Método  de String

'''
import math

def convertToBinary(text):
    list_of_binary_value_of_text = []
    for caracter in text:
        decimal_value_ascii = ord(caracter)
        binary_value_8_bits = format(decimal_value_ascii, '08b')
        list_of_binary_value_of_text.append(binary_value_8_bits)
    return "".join(list_of_binary_value_of_text)


def permutationKeyPC1(key):
    binary_value_of_key = convertToBinary(key)
    pc1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15, 
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29, 
        21, 13, 5, 28, 20, 12, 4]
    sorted_key = []
    for index in pc1:
        sorted_key.append(binary_value_of_key[index-1])
    return "".join(sorted_key)

#Falta montar a tabela de permutação
def permutationKeyPC2(key):
    pc2 = [
        14,17,11,24,1,5,
        3,28,15,6,21,10,
        23,19,12,4,26,8,
        16,7,27,20,13,2,
        41,52,31,37,47,55,
        30,40,51,45,33,48,
        44,49,39,56,34,53,
        46,42,50,36,29,32]

    sorted_key = []
    for index in pc2:
        sorted_key.append(key[index-1])
    return "".join(sorted_key)
    pass

def shiftCycleToLeft(key, number):
    key = list(key)
    for cont in range(number):
        bit0 =key[0]
        key.pop(0)
        key.append(bit0)
    return "".join(key)

# Gerar um array 16 posições de 28 bits type c
def generateSomeKeysTypeC(key):
    c = []
    for index in range(math.floor(len(key)/2)):
        c.append(key[index])
    return "".join(c)

# Gerar um array 16 posições de 28 bits  type d
def generateSomeKeysTypeD(key):
    d = []
    for index in range(math.floor(len(key)/2),len(key)):
         d.append(key[index])
    return "".join(d)

#Gera todas as 16 chaves passando como argumento a anterior
def generateAll16Keys(originalKey):
    #Primeira chave é a original
    key_list = []
    key_list.append(originalKey)


    c0 = generateSomeKeysTypeC(originalKey)
    d0 = generateSomeKeysTypeD(originalKey)

    #Fazendo shift e concatenando
    c1 = shiftCycleToLeft(c0, 1)
    d1 = shiftCycleToLeft(d0, 1)
    k1 = c1+d1
    #Encontrando as chaves
    k1 = permutationKeyPC2(k1)
    key_list.append(k1)

    c2 = shiftCycleToLeft(c1, 1)
    d2 = shiftCycleToLeft(d1, 1)
    k2 = c2+d2
    #Encontrando as chaves
    k2 = permutationKeyPC2(k2)
    key_list.append(k2)

    c3 = shiftCycleToLeft(c2, 2)
    d3 = shiftCycleToLeft(d2, 2)
    k3 = c3+d3
    #Encontrando as chaves
    k3 = permutationKeyPC2(k3)
    key_list.append(k3)
    
    c4 = shiftCycleToLeft(c3, 2)
    d4 = shiftCycleToLeft(d3, 2)
    k4 = c4+d4
    #Encontrando as chaves
    k4 = permutationKeyPC2(k4)
    key_list.append(k4)

    
    c5 = shiftCycleToLeft(c3, 2)
    d5 = shiftCycleToLeft(d3, 2)
    k5 = c5+d5
    #Encontrando as chaves
    k5 = permutationKeyPC2(k5)
    key_list.append(k5)

    c6 = shiftCycleToLeft(c5, 2)
    d6 = shiftCycleToLeft(d5, 2)
    k6 = c6+d6
    #Encontrando as chaves
    k6 = permutationKeyPC2(k6)
    key_list.append(k6)

    c7 = shiftCycleToLeft(c6, 2)
    d7 = shiftCycleToLeft(d6, 2)
    k7 = c7+d7
    #Encontrando as chaves
    k7 = permutationKeyPC2(k7)
    key_list.append(k7)

    c8 = shiftCycleToLeft(c7, 2)
    d8 = shiftCycleToLeft(d7, 2)
    k8 = c8+d8
    #Encontrando as chaves
    k8 = permutationKeyPC2(k8)
    key_list.append(k8)
    
    c9 = shiftCycleToLeft(c8, 1)
    d9 = shiftCycleToLeft(d8, 1)
    k9 = c9+d9
    #Encontrando as chaves
    k9 = permutationKeyPC2(k9)
    key_list.append(k9)

    c10 = shiftCycleToLeft(c9, 2)
    d10 = shiftCycleToLeft(d9, 2)
    k10 = c10+d10
    #Encontrando as chaves
    k10 = permutationKeyPC2(k10)
    key_list.append(k10)

    c11 = shiftCycleToLeft(c10, 2)
    d11 = shiftCycleToLeft(d10, 2)
    k11 = c11+d11
    #Encontrando as chaves
    k11 = permutationKeyPC2(k11)
    key_list.append(k11)

    c12 = shiftCycleToLeft(c11, 2)
    d12 = shiftCycleToLeft(d11, 2)
    k12 = c12+d12
    #Encontrando as chaves
    k12 = permutationKeyPC2(k12)
    key_list.append(k12)

    c13 = shiftCycleToLeft(c12, 2)
    d13 = shiftCycleToLeft(d12, 2)
    k13 = c13+d13
    #Encontrando as chaves
    k13 = permutationKeyPC2(k13)
    key_list.append(k13)

    c14 = shiftCycleToLeft(c13, 2)
    d14 = shiftCycleToLeft(d13, 2)
    k14 = c14+d14
    #Encontrando as chaves
    k14 = permutationKeyPC2(k14)
    key_list.append(k14)
    
    c15 = shiftCycleToLeft(c14, 2)
    d15 = shiftCycleToLeft(d14, 2)
    k15 = c15+d15
    #Encontrando as chaves
    k15 = permutationKeyPC2(k15)
    key_list.append(k15)

    c16 = shiftCycleToLeft(c15, 1)
    d16 = shiftCycleToLeft(d15, 1)
    k16 = c16+d16
    #Encontrando as chaves
    k16 = permutationKeyPC2(k16)
    key_list.append(k16)
    return key_list
    
def permutationIPOfMessage(message):
    binary_value_of_message = convertToBinary(message)
    pc1 = [
        58,50,42,34,26,18,10,2,
        60,52,44,36,28,20,12,4,
        62,54,46,38,30,22,14,6,
        64,56,48,40,32,24,16,8,
        57,49,41,33,25,17,9,1,
        59,51,43,35,27,19,11,3,
        61,53,45,37,29,21,13,5,
        63,55,47,39,31,23,15,7
    ]
    sorted_message = []
    for index in pc1:
        sorted_message.append(binary_value_of_message[index-1])
    return "".join(sorted_message)

def separateMessageToLeft(originalMessage):
    left = []
    for index in range(math.floor(len(originalMessage)/2)):
        left.append(originalMessage[index])
    return "".join(left)

def separateMessageToRight(originalMessage):
    right = []
    for index in range(math.floor(len(originalMessage)/2)):
        right.append(originalMessage[index])
    return "".join(right)

def incrementBitsToXorOperation(textoToIncrement):
    E = [
        32,1,2,3,4,5,
        4,5,6,7,8,9,
        8,9,10,11,12,13,
        12,13,14,15,16,17,
        16,17,18,19,20,21,
        20,21,22,23,24,25,
        24,25,26,27,28,29,
        28,29,30,31,32,1
    ]
    sorted_textoToIncrement = []
    for index in E:
        sorted_textoToIncrement.append(textoToIncrement[index-1])
    return "".join(sorted_textoToIncrement)

def XOR(binaryA, binaryB, size):
    res = []
    for bit in range(size):
        if binaryA[bit] == binaryB[bit]:
            res.append('0')
        else:
            res.append('1')
    return "".join(res)

def s1(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS1 = [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ]
    binary_value_4_bits = format(tabelaS1[linha][coluna], '04b')

    return binary_value_4_bits

def s2(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS2 = [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ]
    binary_value_4_bits = format(tabelaS2[linha][coluna], '04b')

    return binary_value_4_bits

def s3(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS3 = [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ]
    binary_value_4_bits = format(tabelaS3[linha][coluna], '04b')

    return binary_value_4_bits

def s4(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS4 = [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ]
    binary_value_4_bits = format(tabelaS4[linha][coluna], '04b')

    return binary_value_4_bits

def s5(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS5 = [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ]
    binary_value_4_bits = format(tabelaS5[linha][coluna], '04b')

    return binary_value_4_bits

def s6(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS6 = [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ]
    binary_value_4_bits = format(tabelaS6[linha][coluna], '04b')

    return binary_value_4_bits
def s7(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS7 = [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ]
    binary_value_4_bits = format(tabelaS7[linha][coluna], '04b')

    return binary_value_4_bits

def s8(bits):
    linha = int(bits[0]+bits[len(bits)-1],2)
    coluna = int("".join(bits[1:len(bits)-1]),2)
    tabelaS8 = [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
    binary_value_4_bits = format(tabelaS8[linha][coluna], '04b')

    return binary_value_4_bits

def permutationPToValuesSs(bits):
    p = [
        16,7,20,21,
        29,12,28,17,
        1,15,23,26,
        5,18,31,10,
        2,8,24,14,
        32,27,3,9,
        19,13,30,6,
        22,11,4,25
    ]
    sorted_message = []
    for index in p:
        sorted_message.append(bits[index-1])
    return "".join(sorted_message)


#Em desenvolvimento -slide 35
def funcaoPadrao(Rant,keyDaIteracao):
    #Incrementa os bits de 32 para 48 bits
    Rant = incrementBitsToXorOperation(Rant)
    #Faz um XOR com o Rant e KeyN
    xorBetweenRantAndKey = XOR(Rant, keyDaIteracao,48)
    #Função lamba para separar e ter 8 listas de 6 bits cada
    functionToSeparate= lambda test_list, x: [test_list[i:i+x] for i in range(0, len(test_list), x)]
    #Lista com os bits separados
    listSeparateIn8ListBy6 = functionToSeparate(list(xorBetweenRantAndKey), 6)
    resS1 = s1("".join(listSeparateIn8ListBy6[0]))
    resS2 = s2("".join(listSeparateIn8ListBy6[1]))
    resS3 = s3("".join(listSeparateIn8ListBy6[2]))
    resS4 = s4("".join(listSeparateIn8ListBy6[3]))
    resS5 = s5("".join(listSeparateIn8ListBy6[4]))
    resS6 = s6("".join(listSeparateIn8ListBy6[5]))
    resS7 = s7("".join(listSeparateIn8ListBy6[6]))
    resS8 = s8("".join(listSeparateIn8ListBy6[7]))
    resConcatted = resS1+resS2+resS3+resS4+resS5+resS6+resS7+resS8
    resPermutted = permutationPToValuesSs(resConcatted)
    
    return resPermutted

#Ainda em desenvolvimento
#Funcao que vai retornar o valor cifrado
def iterationsAboutMessage(message,keys_list):
    messagePermutated = permutationIPOfMessage(message)
    L = separateMessageToLeft(messagePermutated)
    R = separateMessageToRight(messagePermutated)
    cont = 1
    numberInterations = 16
    while cont<=numberInterations:
        tmp = L
        #L recebe o valor do R da iteracao anterior
        L = R

        #Rant é uma variavel para guardar o valor de R anterior para fazer o aumento
        # de bits para a funcao f
        Rant = R
        R = XOR(tmp, funcaoPadrao(Rant,keys_list[cont]),32) 
        cont=cont+1
    return R+L

def permutationIP1OfMessage(message):
    ip1 = [
        40,8,48,16,56,24,64,32,
        39,7,47,15,55,23,63,31,
        38,6,46,14,54,22,62,30,
        37,5,45,13,53,21,61,29,
        36,4,44,12,52,20,60,28,
        35,3,43,11,51,19,59,27,
        34,2,42,10,50,18,58,26,
        33,1,41,9,49,17,57,25
    ]
    sorted_message = []
    for index in ip1:
        sorted_message.append(message[index-1])
    return "".join(sorted_message)

def joinBits(message):
    tmp = []
    for caracter in message:
        x = "".join(caracter)
        tmp.append(x)
    return tmp


def main():
    message = input("Digite uma mensagem de 8 caracteres:")
    key = input("Digite sua chave de 8 caracteres:")
    keysUseful = generateAll16Keys(permutationKeyPC1(key))
    messageWithIteration = iterationsAboutMessage(message,keysUseful)
    messageCryptedInBinary = permutationIP1OfMessage(messageWithIteration)

    functionToSeparate= lambda test_list, x=4: [test_list[i:i+x] for i in range(0, len(test_list), x)]
    bitsUnion = joinBits(functionToSeparate(messageCryptedInBinary))
    messageCrypted = []
    for caracter in bitsUnion:
        value_hex = hex(int(caracter,2))[2:]
        messageCrypted.append(value_hex)
    print("Mensagem Cifrada:"+"".join(messageCrypted))




if __name__ == '__main__':
    main()

