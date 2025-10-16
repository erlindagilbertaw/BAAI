#
# Erlinda韋琳達, 2025/09/24
# File: Erlinda_Excel.py
# Calculate sum of column in Excel file
#

import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process
#Sum = df['Units Sold'].sum()
#Sum = df.select_dtypes(include='number').sum()
#df_with_total = pd.concat([df, pd.DataFrame([sum])], ignore_index=True)
sums = df.select_dtypes(include='number').sum()

# Optonally give a label for the row (e.g., 'Total')
sums['Name'] = 'Total'

# Append the total of row to the DataFrame
df_with_total = pd.concat([df, pd.DataFrame([sums])], ignore_index=True)

# 3. Output
#print(f'Sum{Sum}')
#print(f'Sum{Sum}')
#print(df_with_total)
print(df_with_total)
df_with_total.to_excel('output.xlsx',index=False)