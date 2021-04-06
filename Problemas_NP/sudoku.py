def is_solucao(tabuleiro, numero, posicao):        
        
    for i in range(len(tabuleiro[0])):
            if tabuleiro[posicao[0]][i] == numero and posicao[1] != i:
                return False        
        
    for i in range(len(tabuleiro)):
        if tabuleiro[i][posicao[1]] == numero and posicao[0] != i:
            return False

    box_x = posicao[1] // 3
    box_y = posicao[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if tabuleiro[i][j] == numero and (i,j) != posicao:
                return False
    
        return True

def achar_vazio(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                return (i, j)
        
    return None

def _existe_solucao_para(tabuleiro) -> bool:
    encontrar = achar_vazio(tabuleiro)
    if not encontrar:
        return True
    else:
        linha, coluna = encontrar
        
    for i in range(1, 10):
        if is_solucao(tabuleiro, i, (linha,coluna)):
            tabuleiro[linha][coluna] = i

            if _existe_solucao_para(tabuleiro):
                return True
                
            tabuleiro[linha][coluna] = 0
        
    return False

def mostrar_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - -")

            for j in range(len(tabuleiro[0])):
                if j % 3 == 0 and j != 0: 
                    print(" | ", end="")

                if j == 8:
                    print(tabuleiro[i][j])
                else:
                    print(str(tabuleiro[i][j]) + " ", end="")
    
tabuleiro = [ 
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
    ]
        
mostrar_tabuleiro(tabuleiro)
print('\n')
print(_existe_solucao_para(tabuleiro))
print('\n')
mostrar_tabuleiro(tabuleiro)
        
        
