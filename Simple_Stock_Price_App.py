import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App""")
st.write("""SEARCH YOUR Ticker Symbol OF COMPANY :  https://stockanalysis.com/stocks/ """,)
tickerSymbol = st.text_input('ENTER Ticker Symbol OF COMPANY :')
start_d = st.date_input()
end_d = st.date_input()


if st.button('Search'):
    st.write("""
    Shown are the stock **closing price** and ***volume*** of Ticker Symbol
    """,tickerSymbol)

    # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
    #define the ticker symbol
    #tickerSymbol = 'GOOGL'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)
    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)
