"""
CSV
first column must be id
last column must be "Yes" or "No"
"""

import pandas

df = pandas.read_csv("tennis.csv")
Z = ['Overcast', 'Mild', 'Normal', 'Weak']

n = len(df)
w = len(Z)

nYes = 0
nNo = 0;

a = []
for i in range(2):
    a.append([])
    for j in range(w):
        a[i].append(0)

for x in range(0, n):
    if df.iloc[x].iat[w + 1] == 'Yes':
        nYes = nYes + 1
        for y in range(0, w):
            if df.iloc[x].iat[y + 1] == Z[y]:
                a[0][y] = a[0][y] + 1
    if df.iloc[x].iat[w + 1] == 'No':
        nNo = nNo + 1
        for y in range(0, w):
            if df.iloc[x].iat[y + 1] == Z[y]:
                a[1][y] = a[1][y] + 1
print(a)
for i in range(w):
    a[0][i] = a[0][i] / nYes
    a[1][i] = a[1][i] / nNo

pYes = nYes / n
pNo = nNo / n

pPlayTennis = 1 * pYes
pNotPlayTennis = 1 * pNo

for i in range(w):
    pPlayTennis = pPlayTennis * a[0][i]
    pNotPlayTennis = pNotPlayTennis * a[1][i]
print(a)
print("pPlayTennis = " + str(pPlayTennis))
print("nNotPlayTennis = " + str(pNotPlayTennis))
