import pandas as pd
import numpy as np
import yfinance as yf








# ************* get SP 500 financial series *************

def get_sp_500(T: int, start: str = '1993-02-01', end: str = '2022-01-01', log_returns: bool = False, freq: int = 1):

    df = yf.download('SPY', start = start, end = end)

    df = df.iloc[::freq, :]
    
    if log_returns:
        df['log_returns'] = np.log1p(df['Close'].pct_change())
    
        return df['log_returns'].dropna().head(T)
    
    return df.head(T)
    

