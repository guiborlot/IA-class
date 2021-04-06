n1, n2 = [], []
def eh_possivel_transportar(objetos:[int], transportes: [int]) -> bool:
    while len(objetos) != 0 and len(transportes) != 0:
        if(objetos[0] < transportes[0]):
            transportes[0] -= objetos[0]
            del(objetos[0])
        elif(objetos[0] > transportes[0]):
            objetos[0] -= transportes[0]
            del(transportes[0])
        else:
            del(objetos[0])
            del(transportes[0])
    if(len(objetos) != 0):
        return False
    else:
        return True
n1, n2 = list(map(int, input().split())), list(map(int, input().split()))

print(eh_possivel_transportar(n1, n2))
