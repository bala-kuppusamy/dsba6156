# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'pandas101'))
	print(os.getcwd())
except:
	pass
#%%
import pandas as pd
import re

print(os.getcwd())

df = pd.read_csv('C:\\Java\\Python\\dsba6156\\pandas101\\pokemon_data.csv')
print(df.head(3))


#%%
print(df['Name'][1:10])
print(df.iloc[2, 3])


#%%
for index, row in df.iterrows():
    if index < 5:
        print(index, row['Name'])


#%%
df.loc[(df['Type 1'] == 'Fire') & (df['Legendary'] == False)]


#%%
df.sort_values('Name', ascending=False)


#%%
df.sort_values(['Type 1', 'Name'], ascending=[False, True])


#%%
df['Total'] = df['HP'] + df['Attack']

df.head(3)


#%%
df['Total2'] = df.iloc[:, 4:10].sum(axis=1)

df.head(3)


#%%
cols = list(df.columns)
df2 = df[cols[0:4] + [cols[-2]] + cols[4:12]]

df2.head(3)


#%%
df.to_csv('poke_2.csv', index=False)


#%%
df2 = df.loc[(df['Type 1'] == 'Fire') & (df['Legendary'] == False)]

df2.reset_index(drop=True, inplace=True)
df2.head(5)


#%%
df3 = df.loc[df['Name'].str.contains('Mega')]
df3.head(5)


#%%
df3 = df.loc[~df['Name'].str.contains('Mega')]
df3.head(5)


#%%
df4 = df.loc[df['Type 1'].str.contains('Grass|Water', regex=True)]
print(df4.head(5))

df5 = df.loc[df['Type 1'].str.contains('grass|water', flags=re.I, regex=True)]
print(df5.head(5))

df5 = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
df5.head(5)


#%%
df.loc[df['Type 1'] == 'Normal', 'Type 1'] = 'aNormal'
df.head(25)


#%%
df.loc[df['Type 1'] == 'aNormal', ['Type 2', 'HP']] = ['Some new type', '260978']
df.head(25)


#%%
df = pd.read_csv('poke_2.csv')
df.head(25)


#%%
df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)


#%%
df.groupby(['Type 1', 'Type 2']).mean()


#%%
for df in pd.read_csv('poke_2.csv', chunksize=5):
    print(df)


#%%
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('poke_2.csv', chunksize=500):
    counts = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, counts])

print(new_df)


