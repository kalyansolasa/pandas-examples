import pandas as pd
import numpy as np
data = [['john',10, 'M'],['doe',None, 'M'],['jessy',13, 'F'], ['visu', 11]]
df = pd.DataFrame(data,columns=['Name','Age', 'Gender'])
print('data frame is :')
print('##'*20)
print(df)
# while running we should not have nill in source column


df['Age'] = df['Age'].fillna(-1)
df['Age'] = df.Age.astype(int)

print('After converting to integer')

print(df['Age'])


df['Age'] = df.Age.astype(float)
print('After converting to float')
print(df['Age'])



df['Age'] = df.Age.astype(str)
print('After converting to string')
print(df['Age'])

df['Age'] = df['Age'].replace('-1.0', np.nan)
print(df['Age'])






