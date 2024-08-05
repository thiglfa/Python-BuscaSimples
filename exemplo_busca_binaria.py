import time

def busca_primaria(conjunto: list, valor: object) -> int:
    ini = 0
    fim = len(conjunto) - 1

    while ini <= fim:
        meio = (ini + fim) // 2
        if conjunto[meio] < valor:
            ini = meio + 1
        elif conjunto[meio] > valor:
            fim = meio - 1
        else:
            return meio
        
    return -1