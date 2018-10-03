import pandas as pd
data = [['john',10, 'M'],['doe',12.5, 'M'],['jessy',13, 'F'], ['visu', 11]]
df = pd.DataFrame(data,columns=['Name','Age', 'Gender'])
print('data frame is :')
print('##'*20)
print(df)
# while running we should not have nill in source column

df['Age'] = df.Age.astype(int,errors='ignore')

print('After converting to integer')
print(df['Age'])


df['Age'] = df.Age.astype(float,errors='ignore')
print('After converting to float')
print(df['Age'])





