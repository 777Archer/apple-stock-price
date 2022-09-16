import yfinance as yf
import streamlit as st
import pandas as pd

# Stock Price App
st.write("""
# Stock App

These are Apple's **closing stock** price and its **volume** from January 1, 2010 to August 31, 2022

""")

# Ticker symbol
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)

# The historical prices
tickerDf = tickerData.history(period= '1d', start='2010-1-01', end='2022-8-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
 """)
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
