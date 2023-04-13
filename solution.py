import pandas as pd
import numpy as np

from statsmodels.stats.weightstats import ztest

chat_id = 1379613676 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    return ztest(x, value=300.59252496635514, alternative='smaller')[1] < 0.1

# historical_db = pd.read_csv("hyp3_historical_data.csv", index_col=0)

# print(historical_db.iloc[0].mean())
