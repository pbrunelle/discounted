# discounted
Simple Discounted Cash Flow Analysis in Python

# Getting started

```bash
python3.8 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run tests:

```bash
python -m pytest tests/*py
```

To compute specific DCF analyses:

```bash
$ ./mo.py

Adj EPS PV: base=2018-2020, debt=naive, shares=constant, terminal-value=0
      -0.01  -0.02  -0.03  -0.04  -0.05  -0.1
0.0   225.2  104.7   64.5   44.4   32.4   8.3
0.01  150.2   87.7   59.1   42.8   32.3   9.4
0.02  108.3   73.5   53.4   40.4   31.5  10.3
0.03   83.4   62.2   47.9   37.8   30.3  11.0
0.04   67.4   53.4   43.0   35.1   28.9  11.5
0.05   56.3   46.5   38.8   32.5   27.4  11.8
```

# Glossary

Here's a short list of acronyms I use (and misuse):

- DCF: discounted cash flow
- PV: present value
