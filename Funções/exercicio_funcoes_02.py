# Crie funções que duplicam, triplicam e quadruplicam o número
# recebido como parâmetro.

def crar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


