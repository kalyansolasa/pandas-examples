import pandas as pd

import pandas as pd
data = [['john',10, 'M'],['doe',None, 'M'],['jessy',13, 'F'], ['visu', 11]]
df = pd.DataFrame(data,columns=['Name','Age', 'Gender'])
print('##'*20)
print('data frame is:')
print(df)


nans = lambda dt: dt[dt.isnull().any(axis=1)]
print('##'*20)
print('rows having null values')
print(nans(df))


