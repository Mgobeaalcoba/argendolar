from typing import List

import requests

import pandas as pd

from tipo_dolares import TipoDivisas


class Argendolar:
    def __init__(self):
        self.base_url = "https://dolarapi.com"
        self.historico_url = "https://api.argentinadatos.com"

    def get_dolar(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        return df

    def get_oficial(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares/oficial"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_blue(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares/blue"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_mep(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares/bolsa"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_ccl(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares/contadoconliqui"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_tarjeta(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares/tarjeta"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_mayorista(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares/mayorista"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_cripto(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/dolares/cripto"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_euro(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/cotizaciones/eur"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_real(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/cotizaciones/brl"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_chileno(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/cotizaciones/clp"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_uruguayo(self) -> pd.DataFrame:
        url = f"{self.base_url}/v1/cotizaciones/uyu"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_dolar_historico(self, tipo: TipoDivisas, fecha: str) -> pd.DataFrame:
        url = f"{self.historico_url}/v1/cotizaciones/dolares/{tipo.value}/{fecha}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_dolar_historia_completa(self, tipo: TipoDivisas) -> pd.DataFrame:
        url = f"{self.historico_url}/v1/cotizaciones/dolares/{tipo.value}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        return df
