#!/usr/bin/env python

import dcf
import pandas as pd

growth_rates = [-0.01, -0.02, -0.03, -0.04, -0.05, -0.06, -0.07]
discount_rates = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05]
adj_earnings_2020 = 8.08  # billion dollars
share_price = 41.06  # dollars
shares = 1.86  # billion

market_cap = share_price * shares

if __name__ == '__main__':
    df = dcf.dcf(adj_earnings_2020, growth_rates, discount_rates)
    pd.set_option('display.float_format', '{:.1f}'.format)
    print(df)
