import pandas as pd

data = {
    'title': [
        'Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E', 'Movie F',
        'Movie G', 'Movie H', 'Movie I', 'Movie J', 'Movie K', 'Movie L'
    ],
    'revenue': [
        3000000, 1500000, 2500000, 4000000, 1000000, 500000,
        3500000, 800000, 2200000, 1800000, 2900000, 700000
    ],
    'budget': [
        800000, 200000, 900000, 700000, 500000, 300000,
        600000, 150000, 400000, 950000, 700000, 250000
    ],
    'runtime': [
        120, 95, 110, 140, 85, 75,
        130, 100, 115, 90, 105, 88
    ]
}

df = pd.DataFrame(data)
bool_series = (df['revenue'] > 2000000) & (df['budget'] < 1000000)
print(df[bool_series])
