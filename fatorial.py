# programa da função fatorial
def fatorial(x, show=False):
    """"
    ∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗
    『 Calcula o fatorial de um número 』
    :param x: número utilizado.
    :param show: pode mostrar a conta ou não.
    ∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗
    """
    n = 1
    for c in range(x, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        n *= c
    return n



# programa principal
print((fatorial(9, show=True)))
help(fatorial)