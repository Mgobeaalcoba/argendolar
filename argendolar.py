import requests

from tipo_dolares import TipoDivisas

from typing import List


class Argendolar:
    def __init__(self):
        self.base_url = "https://dolarapi.com"
        self.historico_url = "https://api.argentinadatos.com"

    def get_dolar(self) -> dict:
        url = f"{self.base_url}/v1/dolares"
        response = requests.get(url)
        data = response.json()
        return data

    def get_oficial(self) -> dict:
        url = f"{self.base_url}/v1/dolares/oficial"
        response = requests.get(url)
        data = response.json()
        return data

    def get_blue(self) -> dict:
        url = f"{self.base_url}/v1/dolares/blue"
        response = requests.get(url)
        data = response.json()
        return data

    def get_mep(self) -> dict:
        url = f"{self.base_url}/v1/dolares/bolsa"
        response = requests.get(url)
        data = response.json()
        return data

    def get_ccl(self) -> dict:
        url = f"{self.base_url}/v1/dolares/contadoconliqui"
        response = requests.get(url)
        data = response.json()
        return data

    def get_tarjeta(self) -> dict:
        url = f"{self.base_url}/v1/dolares/tarjeta"
        response = requests.get(url)
        data = response.json()
        return data

    def get_mayorista(self) -> dict:
        url = f"{self.base_url}/v1/dolares/mayorista"
        response = requests.get(url)
        data = response.json()
        return data

    def get_cripto(self) -> dict:
        url = f"{self.base_url}/v1/dolares/cripto"
        response = requests.get(url)
        data = response.json()
        return data

    def get_euro(self) -> dict:
        url = f"{self.base_url}/v1/cotizaciones/eur"
        response = requests.get(url)
        data = response.json()
        return data

    def get_real(self) -> dict:
        url = f"{self.base_url}/v1/cotizaciones/brl"
        response = requests.get(url)
        data = response.json()
        return data

    def get_chileno(self) -> dict:
        url = f"{self.base_url}/v1/cotizaciones/clp"
        response = requests.get(url)
        data = response.json()
        return data

    def get_uruguayo(self) -> dict:
        url = f"{self.base_url}/v1/cotizaciones/uyu"
        response = requests.get(url)
        data = response.json()
        return data

    def get_dolar_historico(self, tipo: TipoDivisas, fecha: str) -> List[dict]:
        print("Tipo de divisas:", tipo)
        print("Fecha:", fecha)
        print(tipo.value)
        url = f"{self.historico_url}/v1/cotizaciones/dolares/{tipo.value}/{fecha}"
        print(url)
        response = requests.get(url)
        type(response)
        data = response.json()
        return data

    def get_dolar_historia_completa(self, tipo: TipoDivisas) -> List[dict]:
        url = f"{self.historico_url}/v1/cotizaciones/dolares/{tipo.value}"
        response = requests.get(url)
        data = response.json()
        return data
