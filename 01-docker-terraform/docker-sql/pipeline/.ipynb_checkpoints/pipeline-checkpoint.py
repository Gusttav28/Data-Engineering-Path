import sys
import pandas as pd

# print("helo pipeline", sys.argv[1])

month = int(sys.argv[1])

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = month
# pd.DataFrame()
df.to_parquet(f"ooutpout_{month}.parket")
print(df.head())

# df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

# print(f'hello world, month={month}')
 