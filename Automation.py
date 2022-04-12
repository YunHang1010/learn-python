import pandas as pd
from pathlib import Path

df = pd.read_excel('filePath.xlsx',header=None)
df

df = pd.read_excel('filePath.xlsx',header=None)
df

print('总计 = ',df.iloc[9,1])

df = pd.read_excel('filePath.xlsx',header=None)
total = df.loc[df[0] == '总计']

row = {}
row['时间'] = df.iloc[1,0]
row['单价'] = total.iloc[0,1]
row['数量'] = total.iloc[0,2]
row['金额'] = total.iloc[0,3]
print(row)

df_all = pd.DataFrame([row])
df_all

writer = pd.ExcelWriter('/Users/sunyunhang/Desktop/expenses/2.11.xls',engine = 'xlwt')
df_all.to_excel(writer)
writer.save()


CWD = 'filePath'
p = Path(CWD)

for q in p.glob('**/[!All]*.xlsx'):
    print(q.name)


rows = []

for q in p.glob('**/[!All]*.xlsx'):
    df = pd.read_excel(q , header=None)
    total = df.loc[df[0] == '总计']

    row = {}
    row['时间'] = df.iloc[1,0]
    row['单价'] = total.iloc[0,1]
    row['数量'] = total.iloc[0,2]
    row['金额'] = total.iloc[0,3]

    print(row)
    rows.append(row)