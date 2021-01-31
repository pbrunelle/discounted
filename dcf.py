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
    return ret

def pv(series, rate):
    ret = 0.0
    discount = 1.0
    for v in series:
        discount = discount * (1.0 - rate)
        ret += v * discount
    return ret

def dcf(initial, growth_rates, discount_rates):
    df = pd.DataFrame(columns=[str(x) for x in growth_rates], index=[str(x) for x in discount_rates])
    for growth_rate in growth_rates:
        series = create_series(initial, growth_rate, 1000)  # 1000 years ~ infinity
        series = series[1:]  # the base year is already known!
        vals = [pv(series, dr) for dr in discount_rates]
        df[str(growth_rate)] = vals
    return df
