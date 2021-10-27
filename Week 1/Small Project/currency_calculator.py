import streamlit as st
import pandas as pd
from PIL import Image
import pandas as pd
import requests
import json
st.title('CURRENCY CONVERTER')
st.header('Welcome to Currency Converter')
currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
input=st.selectbox('Select base currency for conversion',currency_list)
selection=st.selectbox('Select currency you want to convert to',currency_list)
# Retrieving currency data from ratesapi.io
# https://api.ratesapi.io/api/latest?base=AUD&symbols=AUD
@st.cache
def load_data():
    url = ''.join(['https://api.ratesapi.io/api/latest?base=', input, '&symbols=', selection])
    response = requests.get(url)
    data = response.json()
    base_currency = pd.Series( data['base'], name='base_currency')
    rates_df = pd.DataFrame.from_dict( data['rates'].items() )
    rates_df.columns = ['converted_currency', 'price']
    conversion_date = pd.Series( data['date'], name='date' )
    df = pd.concat( [base_currency, rates_df, conversion_date], axis=1 )
    return df

df = load_data()
st.write(df)