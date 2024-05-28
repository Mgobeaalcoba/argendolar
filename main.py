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
    print("Dólar oficial:", oficial)
    print("Dólar blue:", blue)
    print("Dólar MEP:", mep)
    print("Dólar CCL:", ccl)
    print("Dólar tarjeta:", tarjeta)
    print("Dólar mayorista:", mayorista)
    print("Dólar cripto:", cripto)
    print()
    print("Dólar:", dolares)
    print()

    mep_uno_enero = argendolar.get_dolar_historico(TipoDivisas.MEP, "2023/01/01")
    print("Dólar MEP 01/01/2023:", mep_uno_enero)

    mep_hist = argendolar.get_dolar_historia_completa(TipoDivisas.MEP)
    print("Dólar MEP histórico:", mep_hist)


if __name__ == '__main__':
    main()
