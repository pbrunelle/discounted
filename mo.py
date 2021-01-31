#!/usr/bin/env python

import dcf
import pandas as pd
import numpy as np

growth_rates = [-0.01, -0.02, -0.03, -0.04, -0.05, -0.06, -0.07]
discount_rates = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05]
years = [2018, 2019, 2020]
adj_earnings = [7.5239, 7.8880, 8.0800]  # billion dollars
adj_earnings_2018_2020 = np.mean(adj_earnings)
share_price = 41.06  # dollars
shares = 1.86  # billion
market_cap = share_price * shares

if __name__ == '__main__':
    pd.set_option('display.float_format', '{:.1f}'.format)
    # Naive -- compute PV of future adj earnings based on 2020 adj earnings
    df = dcf.dcf(adj_earnings[-1], growth_rates, discount_rates)
    print(df)
    # Naive -- compute PV of future adj earnings based on 2018 - 2020 adj earnings
    df = dcf.dcf(adj_earnings_2018_2020, growth_rates, discount_rates)
    print(df)
