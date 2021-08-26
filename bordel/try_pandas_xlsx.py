import pandas as pd
from pathlib import Path

path = Path(r"D:\OLD_COMP\out_data\Odds_evolution\Tennis Home-Away margins in 2017.xlsx")
df = pd.read_excel(path)