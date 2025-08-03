import pandas as pd
import json
from datetime import datetime, timedelta

hist_len = 60
pred_len = 12
start_date = datetime(2015, 7, 1)

ts_df   = pd.read_csv("wikipeople_unimodal.csv")  
text_df = pd.read_csv("text.csv")      

text_map = dict(zip(text_df["id"], text_df["text"]))

date_range = [start_date + timedelta(days=i) for i in range(len(ts_df))]
if "Date" not in ts_df.columns:
    ts_df.insert(0, "Date", date_range)


people = [col for col in ts_df.columns if col != "Date"][:5]

rows = []
for person in people:
    series = ts_df[person].dropna().tolist()
    max_start = len(series) - hist_len - pred_len + 1

    text = text_map.get(person, "No description available.")

    for i in range(max_start):
        hist = series[i : i + hist_len]
        pred = series[i + hist_len : i + hist_len + pred_len]
        date = date_range[i + hist_len].strftime("%Y/%m/%d")

        rows.append(
            {
                "Idx": person,
                "Date": date,
                "Hist": json.dumps(hist),
                "Pred": json.dumps(pred),
                "Text": text,
            }
        )

pd.DataFrame(rows).to_csv("wikipeople_multimodal.csv", index=False, encoding="utf-8")
print(f"✅ Total {len(rows)} rows, save as wikipeople_multimodal.csv")
