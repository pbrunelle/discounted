"""
Library to perform simple Discounted Cash Flow Analysis
"""

import numpy as np
import pandas as pd

def create_series(initial, rate, steps):
    ret = []
    for s in range(steps):
        v = initial if s == 0 else ret[s-1] * (1.0 + rate)
        ret.append(v)
    return np.array(ret)

def pv(series, rate):
    ret = 0.0
    discount = 1.0
    for v in series:
        discount *= (1.0 - rate)
        ret += v * discount
    return ret

def dcf(initial, growth_rates, discount_rates, debt=0.0, cash=0.0, debt_rate=0.0, years=1000):
    df = pd.DataFrame(columns=[str(x) for x in growth_rates], index=[str(x) for x in discount_rates])
    for growth_rate in growth_rates:
        earnings_series = create_series(initial, growth_rate, years+1)[1:]  # exclude the first (known) year
        # The company goes out of business when yearly debt payments >= earnings
        for idx in range(years):
            if debt * debt_rate >= earnings_series[idx]:
                earnings_series = earnings_series[:idx]
                years = idx - 1
                break
        interest_series = np.array([debt * debt_rate] * years)
        principal_series = np.array([0.0] * (years - 1) + [debt])
        earnings_pv = np.array([pv(earnings_series, dr) for dr in discount_rates])
        interest_pv = np.array([pv(interest_series, dr) for dr in discount_rates])
        principal_pv = np.array([pv(principal_series, dr) for dr in discount_rates])
        df[str(growth_rate)] = earnings_pv - interest_pv - principal_pv + cash
    return df
