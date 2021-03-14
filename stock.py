import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Check Your Stock:

This is the stock ***Closing Price*** and ***Volume*** of Coupang!

""")

tickerSymbol = "CPNG"
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDf = tickerData.history(period="1d", start="2021-3-10", end="2021-3-11")

st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)