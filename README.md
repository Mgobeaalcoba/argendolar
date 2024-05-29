# Argendolar Package

## Description

This package is used to get the exchange rate between the Argentine Peso and the US Dollar and other currencies (Euro, Real, Peso Chileno y Peso Uruguayo). For this, it uses the [Dolar API](https://dolarapi.com) and the [ArgentinaDatos API](https://argentinadatos.com/docs/) and then it converts the obtained data to a Pandas DataFrame for further analysis.

## Installation

To install the package, you can use the following command:

```bash
pip install argendolar
```

## Usage

To use the package, you can import the `Argendolar` class and create an instance of it. 
 
```python
from argendolar import Argendolar, TipoDivisas

# Create an instance of Argendolar
argendolar = Argendolar()
```

## Methods

The `Argendolar` class has the following methods:

- `api_status()`: Get the status of the API.
- `get_dolar()`: Get all the dollars exchange rates: official, blue, mep, ccl, tarjeta, mayorista, etc. 
- `get_dolar_chart()`: Get the dollar exchange sales rate for all the dollars: official, blue, mep, ccl, tarjeta, mayorista.
- `get_oficial()`: Get the official dollar exchange rate.
- `get_blue()`: Get the blue dollar exchange rate.
- `get_mep()`: Get the MEP dollar exchange rate.
- `get_ccl()`: Get the CCL dollar exchange rate.
- `get_tarjeta()`: Get the dollar exchange rate for credit cards.
- `get_mayorista()`: Get the dollar exchange rate for wholesale.
- `get_cripo()`: Get the dollar exchange rate for cripto.
- `get_euro()`: Get the euro exchange rate.
- `get_real()`: Get the real exchange rate.
- `get_chileno()`: Get the peso chileno exchange rate.
- `get_uruguayo()`: Get the peso uruguayo exchange rate.
- `get_dolar_historico()`: Get the historical dollar exchange rate for a specific date and Dollar Type (TipoDivisa.OFICIAL, TipoDivisa.BLUE, TipoDivisa.MEP, TipoDivisa.CCL, TipoDivisa.TARJETA, TipoDivisa.MAYORISTA, TipoDivisa.CRIPTO)
- `get_dolar_historia_completa()`: Get the complete historical dollar exchange rate since 2011.
- `get_dolar_historia_completa_chart()`: Get the complete historical dollar exchange rate since 2011 in a chart.
- `get_inflacion_mensual_historica()`: Get the monthly historical inflation rate since 2000-01.
- `get_inflacion_mensual_historica_chart()`: Get the monthly historical inflation rate since 2000-01 in a chart.
- `get_inflacion_interanual_historica()`: Get the interannual historical inflation rate since 2000-01.
- `get_inflacion_interanual_historica_chart()`: Get the interannual historical inflation rate since 2000-01 in a chart.
- `get_indice_uva_historico()`: Get the historical UVA index since 2016-01.
- `get_indice_uva_historico_chart()`: Get the historical UVA index since 2016-01 in a chart.
- `get_tasa_plazo_fijo_diaria_bancos()`: Get the daily fixed term rate for banks.
- `get_tasa_plazo_fijo_diaria_bancos_chart()`: Get the daily fixed term rate for banks in a chart.
- `get_tasa_promedio_plazo_fijo_historica()`: Get the historical average fixed term rate since 2000-01.
- `get_tasa_promedio_plazo_fijo_historica_chart()`: Get the historical average fixed term rate since 2000-01 in a chart.

All methods initially consult the state of the APIs (`api_status()`) to understand whether or not they can respond to the query. If the API is not active then they return an exception giving visibility to the API crash.

**All methods without the last word chart** return the data in a **Pandas DataFrame** format for a quick and easy analysis or visualization.

**All methods with the last word chart** return the data in a **Matplotlib chart** format for a quick and easy visualization.

## Examples

Here are some examples of how to use the package:

```python
from argendolar import Argendolar

# Create an instance of Argendolar
argendolar = Argendolar()

# Get the official dollar exchange rate
official = argendolar.get_oficial()

# Get the blue dollar exchange rate
blue = argendolar.get_blue()

# Get the MEP dollar exchange rate
mep = argendolar.get_mep()

# Get the CCL dollar exchange rate
ccl = argendolar.get_ccl()

# Get the dollar exchange rate for credit cards
tarjeta = argendolar.get_tarjeta()

# Get the dollar exchange rate for wholesale
mayorista = argendolar.get_mayorista()

# Get the dollar exchange rate for cripto
cripto = argendolar.get_cripo()

# Get the euro exchange rate
euro = argendolar.get_euro()

# Get the real exchange rate
real = argendolar.get_real()

# Get the peso chileno exchange rate
chileno = argendolar.get_chileno()

# Get the peso uruguayo exchange rate
uruguayo = argendolar.get_uruguayo()

# Get the historical dollar exchange rate for a specific date
historico = argendolar.get_dolar_historico(tipo: TipoDivisas.MEP, fecha='2022-01-01')

# Get the complete historical dollar exchange rate since 2011
historia_completa = argendolar.get_dolar_historia_completa()
```

## Contributing

If you want to contribute to this project, you can follow the steps below:

1. Fork the repository to your own GitHub account.
2. Clone the repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them.
5. Push your changes to your forked repository.
6. Create a pull request from your forked repository to the original repository.
7. Wait for the review and approval of your pull request.
8. Once your pull request is approved, your changes will be merged into the main branch of the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, you can contact me at [Mariano Gobea Alcoba](mailto:gobeamariano@gmail.com) or [Mariano Gobea Alcoba](https://www.linkedin.com/in/mariano-gobea-alcoba/).