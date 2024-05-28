import requests

import pandas as pd

from tipo_dolares import TipoDivisas


class Argendolar:
    def __init__(self):
        """
        Initialize the Argendolar class.
        """
        self.base_url = "https://dolarapi.com"
        self.historico_url = "https://api.argentinadatos.com"

    def get_dolar(self) -> pd.DataFrame:
        """
        Get all the dollars exchange rates:
            - Oficial
            - Blue
            - MEP
            - CCL
            - Tarjeta
            - Mayorista
            - Cripto
        And the exchange rates for the following currencies:
            - Euro
            - Real
            - Chileno
            - Uruguayo
        :return: A Pandas DataFrame with the exchange rates
        """
        url = f"{self.base_url}/v1/dolares"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        return df

    def get_oficial(self) -> pd.DataFrame:
        """
        Get the exchange rate for the official dollar.
        :return: A Pandas DataFrame with the exchange rate for the official dollar.
        """
        url = f"{self.base_url}/v1/dolares/oficial"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_blue(self) -> pd.DataFrame:
        """
        Get the exchange rate for the blue dollar.
        :return: A Pandas DataFrame with the exchange rate for the blue dollar.
        """
        url = f"{self.base_url}/v1/dolares/blue"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_mep(self) -> pd.DataFrame:
        """
        Get the exchange rate for the MEP dollar.
        :return: A Pandas DataFrame with the exchange rate for the MEP dollar.
        """
        url = f"{self.base_url}/v1/dolares/bolsa"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_ccl(self) -> pd.DataFrame:
        """
        Get the exchange rate for the CCL dollar.
        :return: A Pandas DataFrame with the exchange rate for the CCL dollar.
        """
        url = f"{self.base_url}/v1/dolares/contadoconliqui"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_tarjeta(self) -> pd.DataFrame:
        """
        Get the exchange rate for the tarjeta dollar.
        :return: A Pandas DataFrame with the exchange rate for the tarjeta dollar.
        """
        url = f"{self.base_url}/v1/dolares/tarjeta"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_mayorista(self) -> pd.DataFrame:
        """
        Get the exchange rate for the mayorista dollar.
        :return: A Pandas DataFrame with the exchange rate for the mayorista dollar.
        """
        url = f"{self.base_url}/v1/dolares/mayorista"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_cripto(self) -> pd.DataFrame:
        """
        Get the exchange rate for the cripto dollar.
        :return: A Pandas DataFrame with the exchange rate for the cripto dollar.
        """
        url = f"{self.base_url}/v1/dolares/cripto"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_euro(self) -> pd.DataFrame:
        """
        Get the exchange rate for the euro.
        :return: A Pandas DataFrame with the exchange rate for the euro.
        """
        url = f"{self.base_url}/v1/cotizaciones/eur"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_real(self) -> pd.DataFrame:
        """
        Get the exchange rate for the real.
        :return: A Pandas DataFrame with the exchange rate for the real.
        """
        url = f"{self.base_url}/v1/cotizaciones/brl"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_chileno(self) -> pd.DataFrame:
        """
        Get the exchange rate for the chileno.
        :return: A Pandas DataFrame with the exchange rate for the 'peso chileno'.
        """
        url = f"{self.base_url}/v1/cotizaciones/clp"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_uruguayo(self) -> pd.DataFrame:
        """
        Get the exchange rate for the 'peso uruguayo'.
        :return: A Pandas DataFrame with the exchange rate for the 'peso uruguayo'.
        """
        url = f"{self.base_url}/v1/cotizaciones/uyu"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_dolar_historico(self, tipo: TipoDivisas, fecha: str) -> pd.DataFrame:
        """
        Get the historical exchange rate for a specific date.
        :param tipo: The type of dollar to get the historical exchange rate for. (TipoDivisas: OFICIAL, BLUE, MEP, MAYORISTA, SOLIDARIO, TURISTA)
        :param fecha: The date to get the historical exchange rate for. (str: "YYYY/MM/DD")
        :return: A Pandas DataFrame with the historical exchange rate for the specified date.
        """
        url = f"{self.historico_url}/v1/cotizaciones/dolares/{tipo.value}/{fecha}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame([data])
        return df

    def get_dolar_historia_completa(self, tipo: TipoDivisas) -> pd.DataFrame:
        """
        Get the complete historical exchange rate since 2011 for a specific type of dollar.
        :param tipo: The type of dollar to get the complete historical exchange rate for. (TipoDivisas: OFICIAL, BLUE, MEP, MAYORISTA, SOLIDARIO, TURISTA)
        :return: A Pandas DataFrame with the complete historical exchange rate for the specified type of dollar.
        """
        url = f"{self.historico_url}/v1/cotizaciones/dolares/{tipo.value}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        return df
