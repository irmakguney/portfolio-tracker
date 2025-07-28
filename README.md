# Portfolio Tracker

A simple and interactive portfolio tracker app built with Python and Streamlit.  
It tracks live stock and cryptocurrency prices, calculates profit and loss, and displays data with interactive charts.

## Features

- Real-time price updates using Yahoo Finance API (`yfinance`)
- Portfolio management with buy quantity and price input
- Profit and loss calculation for each asset
- Interactive visualization with Streamlit and Matplotlib
- Clean and user-friendly interface

## Installation

1. Clone the repository:  
   `git clone https://github.com/irmakguney/portfolio-tracker.git`

2. Create and activate a virtual environment (optional but recommended):  
   ```bash
   python -m venv env  
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install dependencies:  
   `pip install -r requirements.txt`

## Usage

Run the Streamlit app:  
`streamlit run app.py`

Follow the on-screen instructions to add assets and view live portfolio performance.

## Technologies Used

- Python 3.12  
- Streamlit  
- yfinance  
- pandas  
- matplotlib

## Future Improvements

- Add more asset classes (e.g. ETFs, bonds)  
- User authentication and data persistence  
- Export portfolio data as CSV or Excel  
- Enhanced UI/UX design

## Author

Irmak Guney  
[GitHub Profile](https://github.com/irmakguney)  
