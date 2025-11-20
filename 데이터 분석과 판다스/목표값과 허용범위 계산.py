import pandas as pd

file_path = "02_oxide.csv"
oxide_df = pd.read_csv(file_path)

# oxide_df.info()

oxide_thickness = oxide_df["oxide_thickness"]
target_thickness = oxide_thickness.median()

std_thickness = oxide_thickness.std()
print(f"목표값:{target_thickness:.2f}")
print(f"표준 편차:{std_thickness:.2f}")

lower_limit = target_thickness - 3 * std_thickness
upper_limit = target_thickness +3 * std_thickness

print(f"목표값:{target_thickness:.2f}")
print(f"허용 범위:{lower_limit:.2f}~{upper_limit:.2f}")