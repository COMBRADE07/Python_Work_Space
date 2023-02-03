# reading csv file and
import pandas as pd
ok = pd.read_csv('info.csv')
print(ok)



# to_string()
# Tip: use to_string() to print the entire DataFrame.
df2 = pd.read_csv('data_file.csv')
print(df2.to_string())






# max_rows
# You can change the maximum rows number with the same statement. ===   pd.options.display.max_rows=555
# syntax =>   pd.options.display.max_rows

rows = pd.options.display.max_rows
print("Max rows: ", rows)


