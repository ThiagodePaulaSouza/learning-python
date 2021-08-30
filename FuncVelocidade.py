def velocidade(espaco=None, tempo=None):
    v = espaco/tempo
    if (espaco is not None):
        print('o espaço é: {:.2f} m/s' .format (espaco))
    else:
        print('o espaço não foi informado')
    if (tempo is not None):
        print('o tempo é: {:.2f} m/s ' .format (tempo))
    else:
        print('o tempo não foi informado')
    print('a velocidade é: {:.2f} m/s ' .format (v))
print(velocidade(100, 20))