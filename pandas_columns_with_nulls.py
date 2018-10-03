import pandas as pd
data = [['john',10, 'M'],['doe',None, 'M'],['jessy',13, 'F'], ['visu', 11]]
df = pd.DataFrame(data,columns=['Name','Age', 'Gender'])
print('##'*20)
print('data frame is:')
print('##'*20)
print(df)

print('columns having null values')
print('##'*20)
print(df.columns[df.isnull().any()].tolist())


