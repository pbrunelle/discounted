#!/usr/bin/env python

import dcf
import pandas as pd
import numpy as np

growth_rates = [-0.01, -0.02, -0.03, -0.04, -0.05, -0.06, -0.07]
discount_rates = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05]
years = [2018, 2019, 2020]
adj_earnings = [7.5239, 7.8880, 8.0800]  # billion dollars
cash = np.array([1.333, 2.117, 4.945])  # billion dollars
debt = np.array([25.746, 28.042, 29.471])
net_debt = debt - cash
wt_avg_fixed_cpn = 0.0413
wt_avg_yrs = 11.78
share_price = 41.06  # dollars
shares = 1.86  # billion
market_cap = share_price * shares

if __name__ == '__main__':
    pd.set_option('display.float_format', '{:.1f}'.format)
    # Naive -- compute PV of future adj earnings based on 2020 adj earnings
    df = dcf.dcf(adj_earnings[-1], growth_rates, discount_rates)
    print(f"DCF: base=2020, debt=ignored\n{df}")
    # Naive -- compute PV of future adj earnings based on 2018 - 2020 adj earnings
    df = dcf.dcf(np.mean(adj_earnings), growth_rates, discount_rates)
    print(f"DCF: base=2018-2020, debt=ignored\n{df}")
    # Include debt in a naive way:
    # - Assume no changes in debt (no issues, no refis, no repayments)
    # - Compute the present value of debt interest payments
    # - Subtract net debt from PV of fture adj earnings
    df = dcf.dcf(np.mean(adj_earnings), growth_rates, discount_rates, np.mean(debt), np.mean(cash), wt_avg_fixed_cpn)
    print(f"DCF: base=2018-2020, debt=naive\n{df}")
