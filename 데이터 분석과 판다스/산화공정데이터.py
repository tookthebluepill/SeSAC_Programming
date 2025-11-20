import pandas as pd

file_path = "02_oxide.csv"
oxide_df = pd.read_csv(file_path)

oxide_df.info()