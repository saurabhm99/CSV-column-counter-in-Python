import pandas as pd
file=pd.read_csv("name_of_your_file.csv")
col_count = sum(1 for column in file)
print(col_count)
#saurabhm
