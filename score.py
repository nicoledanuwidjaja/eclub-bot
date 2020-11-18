import pandas as pd
import sys

if len(sys.argv) != 2:
    raise Exception("Usage: [.csv file]")

raw = pd.read_csv(sys.argv[1])
judges = raw["Your Name"].drop_duplicates()

# use format of raw table from Google Forms
calculations = raw.groupby("Venture Name", as_index=False).agg({
    "Target Market": "mean",
    "Problem or Need": "mean",
    "Solution": "mean",
    "Team Dynamic": "mean",
    "Revenue Model": "mean",
    "Ingenuity": "mean",
    "Creativity": "mean"}).round(2)

# append tally column and write to new file
calculations["Tally"] = calculations.mean(axis=1, numeric_only=True).round(2)
final_results = calculations.sort_values(by=['Tally'], ascending=False)
final_results.to_csv("final_results.csv", index=False)
