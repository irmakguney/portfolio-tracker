import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Live Portfolio Tracker & P/L Analysis")

if "portfolio" not in st.session_state:
    st.session_state.portfolio = []

with st.form("add_asset", clear_on_submit=True):
    symbol = st.text_input("Symbol (e.g. AAPL, BTC-USD)").upper().strip()
    quantity = st.number_input("Quantity", min_value=1, step=1)
    purchase_price = st.number_input("Purchase Price (USD)", min_value=0.01, step=0.01, format="%.2f")
    submit = st.form_submit_button("Add to Portfolio")

    if submit:
        if symbol and quantity > 0 and purchase_price > 0:
            st.session_state.portfolio.append({
                "symbol": symbol,
                "quantity": quantity,
                "purchase_price": purchase_price
            })
            st.success(f"✅ {symbol} added to portfolio!")
        else:
            st.error("⚠️ Please fill in all fields correctly.")

if st.session_state.portfolio:
    df_portfolio = pd.DataFrame(st.session_state.portfolio)
    st.write("### 📋 Your Portfolio")
    st.dataframe(df_portfolio)

    @st.cache_data(ttl=60)
    def fetch_price(ticker):
        data = yf.download(ticker, period="1d", interval="1m", auto_adjust=True, progress=False)
        if not data.empty and "Close" in data.columns:
            return float(data["Close"].iloc[-1])
        return None

    def pl_analysis(portfolio):
        results = []
        for asset in portfolio:
            current_price = fetch_price(asset["symbol"])
            if current_price is not None:
                pnl = (current_price - asset["purchase_price"]) * asset["quantity"]
                results.append({
                    "Symbol": asset["symbol"],
                    "Purchase Price": asset["purchase_price"],
                    "Quantity": asset["quantity"],
                    "Current Price": current_price,
                    "P/L": pnl
                })
        return pd.DataFrame(results)

    df_analysis = pl_analysis(st.session_state.portfolio)

    if not df_analysis.empty:
        st.write("### 💰 Profit/Loss Analysis")
        st.dataframe(df_analysis.style.applymap(
            lambda x: 'color: green' if isinstance(x, (int,float)) and x > 0 else ('color: red' if isinstance(x, (int,float)) and x < 0 else ''),
            subset=["P/L"]
        ))

        st.write("### 📊 Profit/Loss Chart")
        st.bar_chart(df_analysis.set_index("Symbol")["P/L"])

        st.write("### 📈 Stock Price Charts (Last 1 Day, 5-minute interval)")
        for symbol in df_analysis["Symbol"]:
            data = yf.download(symbol, period="1d", interval="5m", auto_adjust=True, progress=False)
            if not data.empty:
                fig, ax = plt.subplots()
                ax.plot(data.index, data["Close"], label=symbol)
                ax.set_title(f"{symbol} - Last 1 Day Price Chart")
                ax.set_xlabel("Time")
                ax.set_ylabel("Price (USD)")
                ax.legend()
                st.pyplot(fig)
else:
    st.info("📌 Add assets to your portfolio.")

# Manual refresh advice instead of problematic rerun function
st.info("🔄 To update data, please refresh the page manually (browser refresh).")


