from argendolar import Argendolar

from tipo_dolares import TipoDivisas


def main():
    argendolar = Argendolar()
    dolares = argendolar.get_dolar()
    oficial = argendolar.get_oficial()
    blue = argendolar.get_blue()
    mep = argendolar.get_mep()
    ccl = argendolar.get_ccl()
    tarjeta = argendolar.get_tarjeta()
    mayorista = argendolar.get_mayorista()
    cripto = argendolar.get_cripto()
    print(oficial)
    print()
    print(blue)
    print()
    print(mep)
    print()
    print(ccl)
    print()
    print(tarjeta)
    print()
    print(mayorista)
    print()
    print(cripto)
    print()
    print(dolares)
    print()

    mep_uno_enero = argendolar.get_dolar_historico(TipoDivisas.MEP, "2023/01/01")
    print(mep_uno_enero)
    print()

    mep_hist = argendolar.get_dolar_historia_completa(TipoDivisas.MEP)
    print(mep_hist)


if __name__ == '__main__':
    main()
