import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#Simple Stock Price Application

Shown are the stock closing prices and volume of Google!

""")

#Define the ticker symbol
tickerSymbol = "GOOGL"

#Get data on the ticker
tickerData = yf.Ticker(tickerSymbol)

#Get the historical prices for this ticker
tickerDF = tickerData.history(period="id", start="2010-5-31", end="2020-5-31")

#Open high, Low Close Volume Dividends Stock Splits

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)