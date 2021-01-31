#!/usr/bin/env python

"""
A naive DCF model in which we assume:
- Adjusted income == free cash flow
- The company's adj income decreases every year at a constant rate
- The company stops operation as soon as interest burden >= adj income
- At that point, all debt is repaid
- At that point, the company has 0 residual value
- The amount of outstanding debt is fixed (i.e. no issuance, no calls)
- The interest rate is constant (4.13%, taken from DDIS<Go>)
- There are no changes in the number of shares (i.e. no buybacks, no awards)
- The company does not divest or acquire assets

We want to know: what are estimates of today's present value of the company's
shares?
"""

import dcf
import pandas as pd
import numpy as np

growth_rates = [-0.01, -0.02, -0.03, -0.04, -0.05, -0.10]
discount_rates = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05]
years = [2018, 2019, 2020]
key_df = pd.DataFrame.from_records(
    [
        [7.5239, 7.8880, 8.0800],  # billion USD
        [1.333, 2.117, 4.945],  # billion USD,
        [25.746, 28.042, 29.471],  # billion USD
    ],
    columns=[str(x) for x in years],
    index=["adj_earnings", "cash", "debt"]
)
wt_avg_fixed_cpn = 0.0413  # wt_avg_yrs = 11.78
share_price = 41.06  # USD
shares = 1.86  # billion

if __name__ == '__main__':
    print(key_df)
    pd.set_option('display.float_format', '{:.1f}'.format)
    df = dcf.dcf(
        np.mean(key_df.loc["adj_earnings"]),
        growth_rates,
        discount_rates,
        debt=np.mean(key_df.loc["debt"]),
        cash=np.mean(key_df.loc["cash"]),
        debt_rate=wt_avg_fixed_cpn,
    )
    print(f"Adj EPS PV: base=2018-2020, debt=naive, shares=constant, terminal-value=0\n{df / shares}")
